import contextlib
from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import sqlite3

app = Flask(__name__, static_url_path=", static_folder='static', template_folder='templates')

                                      @ app.route("/", methods=['GET'])


def home():
    kwargs = {
        "name": "Dias",
        "name2": "Dina",
        "is_fruit": True,
        "words": ["Python", "Go", "C", "C++"],
        "books": [
            {"id": 1, "title": "Amon Ra", "description": "Amon Ra Amon Ra", "author": "A.Pelevin"},
            {"id": 2, "title": "Amon Ra 1", "description": "Amon Ra 1 Amon Ra 1", "author": "V.Pelevin"},
            {"id": 3, "title": "Amon Ra 2", "description": "Amon Ra 2 Amon Ra 2", "author": "N.Pelevin"},
            {"id": 4, "title": "Amon Ra 3", "description": "Amon Ra 3 Amon Ra 3", "author": "K.Pelevin"},
        ],
        "ids": [5, 6, 8, 0, 12]
    }

    return render_template('pages/home.html', **kwargs)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('pages/book_create.html')
    elif request.method == "POST":
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        author = request.form['author'].strip()

        with contextlib.closing(sqlite3.connect('database.db')) as connection:
            with connection as cursor:
                cursor.execute(
                    "INSERT INTO book_posts (title, description, author) VALUES (?, ?, ?);",
                    (title, description, author)
                )

        return redirect(url_for('book_list'))


@app.route('/list', methods=['GET', "POST"])
def book_list():
    title = request.form.get("title", "").strip()

    with contextlib.closing(sqlite3.connect('database.db')) as connection:
        with connection as cursor:
            rows = cursor.execute("""
SELECT id, title, description, author FROM book_posts
WHERE title LIKE ? ORDER BY id ASC;
            """, (f"%{title}%",))
            records = rows.fetchall()

            _books = []
            for record in records:
                new_dict = {
                    "id": record[0],
                    "title": record[1],
                    "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
                    "author": record[3]
                }
                _books.append(new_dict)

    categories = ["Детективы", "Фентези", "Исторические"]

    return render_template('pages/book_list.html', books=_books, search=title, categories=categories)


@app.route('/detail/<int:pk>', methods=['GET'])
def detail(pk: int):
    """
    Вывод на экран одного поста книг из базе данных
    """

    with sqlite3.connect('database.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT id, title, description, author FROM book_posts WHERE id = ?;", (pk,))
        record = cursor.fetchone()
        _book = {
            "id": record[0],
            "title": record[1],
            "description": record[2],
            "author": record[3]
        }

    return render_template('pages/book_detail.html', book=_book)


@app.route('/delete/<int:pk>', methods=['GET'])
def delete(pk: int):
    """
    Удаление поста из базы данных и возврат ко всем постам
    """

    with sqlite3.connect('database.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM book_posts WHERE id = ?;", (pk,))
    return redirect(url_for('book_list'))


def database_create():
    """
    database - book_shop
    """

    """
CREATE DATABASE book_shop
WITH
OWNER = postgres
ENCODING = 'UTF8'
CONNECTION LIMIT = -1
IS_TEMPLATE = False;
    """

    """
    table - book_posts (id - serial, title - varchar200, description - varchar2000, author - varchar20)
    """

    """
CREATE TABLE public.book_posts
(
    id serial NOT NULL,
    title character varying(200) NOT NULL UNIQUE,
    description character varying(2000) DEFAULT '',
    author character varying(20) DEFAULT '',
    PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS public.book_posts
OWNER to postgres;
    """

    """
SELECT * FROM public.book_posts
ORDER BY id ASC 
    """

    """
INSERT INTO public.book_posts (title, description, author) VALUES ('Мёртвые души', 'Мёртвые души Мёртвые души Мёртвые души', 'Гоголь');
    """
    pass


def sql3_ex():
    with sqlite3.connect('database.db') as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("""
CREATE TABLE IF NOT EXISTS book_posts
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    description TEXT DEFAULT '',
    author TEXT DEFAULT ''
);
            """)

        rows = cursor.execute("""
SELECT * FROM book_posts
ORDER BY id ASC 
""")

        data = rows.fetchall()
        print(data)


if __name__ == '__main__':
    app.run(port=5000)