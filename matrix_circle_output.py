import numpy as np

lst = []
#n = int(input())
n = 5
length = n ** 2
# генерируем матрицу нужного размера
matrix = np.full(( n, n), 0)
# генерируем строку с нужными элементами для вставки в матрицу
for x in range(length):
    lst.append(x+1)
# переводим лист в одномерную матрицу
arr = np.array(lst)

# заполняем первую строку
for x in range(n):
    matrix[0,x] = arr[x]

# выводим матрицу в строки
for z in range(n):
    for w in range(n):
        print(matrix[z,w], end=' ')
    print()

