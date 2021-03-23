import requests
# первоначальный файл из дирректории
file = '699991.txt'


# пересборка URL
def join_url(text):
	base = 'https://stepic.org/media/attachments/course67/3.6.3/'
	ready_link = base + text
	return ready_link


# читаем содержимое файла по адресу URL
def chek_file(url):
	r = requests.get(join_url(url))
	print(r.text)
	return r.text


# первичная сборка и чтение файла
flag = chek_file(file)

# зацикливаем функцию, до появления искомой строки
while 'We' not in flag:
	flag = chek_file(flag)
