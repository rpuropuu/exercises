n = int(input())
matrix = [[0] * n for i in range(n)]
arr, m = 1, 0
# аранее присваиваем значение
# центральному элементу матрицы
matrix[n // 2][n // 2] = n * n
for j in range(n//2):
# заполняем верхнюю строку
    for i in range(n-m):
        matrix[j][i + j] = arr
        arr+=1
# заполняем правого столбца
    for i in range(j+1, n-j):
        matrix[i][-j - 1] = arr
        arr+=1
# заполняем нижнюю строку
    for i in range(j+1, n-j):
        matrix[-j - 1][-i - 1] = arr
        arr+=1
# заполняем левого столбца
    for i in range(j+1, n-(j+1)):
        matrix[-i - 1][j] = arr
        arr += 1
    m += 2
# вывод на экран
for i in matrix:
    print(*i)
