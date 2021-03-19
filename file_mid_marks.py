import os
st = []
arr = []
temp = []
arr_math = []
arr_phys = []
arr_russ = []
# подсчёт строк в файле
s = sum(1 for line in open('.\data\dataset_3363_4(14).txt', 'r'))

# открываем файл и делаем список из строк, удаляя тех символы
inf = open('.\data\dataset_3363_4(14).txt', 'r')
for i in range(s):
   st.append(inf.readline().strip())

for i in range(s):
    arr.append(st[i].split(';'))
with open('.\data\data_ready.txt', 'w') as res:
    for i in range(s):
        #for j in range(3):
        temp = []
        temp.append(arr[i][1])
        temp.append(arr[i][2])
        temp.append(arr[i][3])
        res.write(f'{sum(map(int, temp)) / len(temp)}\n')
        arr_math.append(arr[i][1])
        arr_phys.append(arr[i][2])
        arr_russ.append(arr[i][3])

    res.write(f'{sum(map(int, arr_math)) / s} ')
    res.write(f'{sum(map(int, arr_phys)) / s} ')
    res.write(f'{sum(map(int, arr_russ)) / s}')
    #res.write(f'{round(sum(map(int, arr_math)) / s, 9)} ')
    #res.write(f'{round(sum(map(int, arr_phys)) / s, 9)} ')
    #res.write(f'{round(sum(map(int, arr_russ)) / s, 9)}')
#print(sum(map(int, arr_phys)) / s, end=' ')
#print(sum(map(int, arr_russ)) / s)

