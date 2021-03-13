numbers = int(input())
cnt = 1
mark = 0
for i in range(numbers):
    if mark >= numbers:
        break
    print(cnt, end=' ')
    if numbers == 1:
        break
    cnt += 1
    mark += 1
    for j in range(i+1):
        if mark >= numbers:
            break
        print(cnt, end=' ')
        mark += 1
##########################################
# short of my method
#
# n = int(input())
# print(*[i for i in range(1,n+1) for j in range(i)][:n])
#
##########################################
#
# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])
#
##########################################
#
# import math
#
# x = int(input())
# print(*[int( 1/2 + math.sqrt(2 * n) ) for n in range(1, x + 1)])
#
