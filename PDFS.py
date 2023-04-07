import datetime


gmt_time = datetime.datetime.utcnow()
print("GMT time: ", gmt_time)


local_time = datetime.datetime.now()
print("Local time: ", local_time)

#########################################################

date1 = datetime.date(2022, 3, 1)
date2 = datetime.date(2022, 4, 1)
delta = date2 - date1
print("Days between", date1, "and", date2, "is", delta.days)

#########################################################
date1 = datetime.datetime(2022, 3, 1, 12, 30, 0)
date2 = datetime.datetime(2022, 3, 2, 10, 45, 30)
delta = date2 - date1
print("Time difference between", date1, "and", date2, "is", delta)


days = delta.days
seconds = delta.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60

print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
#########################################################
import calendar


def create_calendar(year, month):

    cal = calendar.monthcalendar(year, month)


    html_calendar = '<table>'
    html_calendar += '<tr><th colspan="7">{0} {1}</th></tr>'.format(calendar.month_name[month], year)
    html_calendar += '<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Вс</th></tr>'

    for week in cal:
        html_calendar += '<tr>'
        for day in week:
            if day == 0:
                html_calendar += '<td></td>'
            else:
                html_calendar += '<td>{0}</td>'.format(day)
        html_calendar += '</tr>'

    html_calendar += '</table>'
    return html_calendar



year = 2023
month = 3


html_calendar = create_calendar(year, month)


print(html_calendar)
#########################################################
emails = ['test@example.com', 'user@gmail.com', 'admin@domain.com']
domains = []
for email in emails:
    domain = email.split('@')[1]
    domains.append(domain)
print(domains)

#########################################################
text = "The quick brown fox jumps over the lazy dog"
vowels = ['a', 'e', 'i', 'o', 'u']
words = text.split()
vowel_words = []
for word in words:
    if word[0].lower() in vowels:
        vowel_words.append(word)
print(vowel_words)
#########################################################


text = "This is a test; this is only a test, do not panic."
delimiters = [' ', ';', ',']
split_text = []
for delimiter in delimiters:
    temp_text = []
    for word in text.split(delimiter):
        if word:
            temp_text.append(word.strip())
    split_text.extend(temp_text)
print(split_text)

#########################################################
candidates = {'Аскаров': 0, 'Бекмуханов': 0, 'Ернур': 0, 'Пешая': 0, 'Карим': 0, 'Шаримазданов': 0}

while True:
    vote = input("Введите имя кандидата, за которого хотите проголосовать (для выхода нажмите Enter): ")
    if not vote:
        break
    if vote in candidates:
        candidates[vote] += 1
        print(f"Вы проголосовали за кандидата {vote}")
    else:
        print("Некорректное имя кандидата")

winner = max(candidates, key=candidates.get)
max_votes = candidates[winner]

if list(candidates.values()).count(max_votes) > 1:
    winners = [name for name, votes in candidates.items() if votes == max_votes]
    winner = sorted(winners, key=len)[0]

print(f"Победитель выборов: {winner} (количество голосов: {candidates[winner]})")
