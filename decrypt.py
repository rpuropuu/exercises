import string

st = 'H14D5p10u2J19q2F19A6u11T15s12d19i18T16I19M18z9x1K12J9I8E1I12v10f6q7j12E14S13l20m5L20Z18a18F8W9'
new_st = ''
arr = []
j = 0
# попарно разбиваем строку на символ + цифра
for i in range(len(st)):
    if st[i] in string.digits:
        new_st += st[i]
    else:
        new_st += ' ' + st[i] + ' '
# по пробелу заводим в список
arr = new_st.split()
# каждых два элемента перемножаем и выводим в одну строку
while j < len(arr):
    print(arr[j] * int(arr[j+1]), end='')
    j += 2

