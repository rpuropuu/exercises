import requests
# копируем URL
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/997.txt') # простой GET запрос
# разбивает весь текст в список по строкам
# можно посмотреть как это выглядит:
# print(r.text.splitlines())
print(len(r.text.splitlines()))

