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

