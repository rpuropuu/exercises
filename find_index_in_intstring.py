lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print('Отсутствует')
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')



############################################
# l, n = [int(i) for i in input().split()], int(input())
# print(*[x for x in range(len(l)) if l[x]==n] if n in l else ["Отсутствует"])
