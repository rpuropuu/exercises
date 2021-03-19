import requests
# копируем URL
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/997.txt') # простой GET запрос
print(len(r.text.splitlines())) # разбивает весь текст в список по строкам
# можно посмотреть как это выглядит:
# print(r.text.splitlines())


