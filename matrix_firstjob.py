import numpy as np

a = []
lst = ''
arr = ''

# вводим первую строку для замера количества столбцов
lst = str(input())

# считаем количество столбцов
length = len(lst.split())

# запускаем цикл с сохранением условий задания и формы матрицы
while lst != 'end' and len(lst.split()) == length:
    arr += lst + ' '
    lst = str(input())

# переводим строки в int
arr = list(map(int, arr.split()))

# переводим список в одномерную матрицу
matrix = np.array(arr)

# записываем столбцы (j) и строки (i)
i = len(arr) // length
j = length
#меняем размерность матрицы
matrix1 = matrix.reshape( i, j)
# создаём нулевую матрицу по заданным размерам
matrix2 = np.full((i,j), 0)
# высчитываем и записываем поверх нулевой матрицы искомые значения
for b in range(j):
    for a in range(i):
        if a+1 == i:
            x = 0
        else:
            x = a + 1
        if b+1 == j:
            y = 0
        else:
            y = b + 1
        matrix2[a,b] = matrix1[a-1,b] + matrix1[x,b] + matrix1[a,b-1] + matrix1[a,y]
# выводим ответ
print()
for z in range(i):
    for w in range(j):
        print(matrix2[z,w], end=' ')
    print()
