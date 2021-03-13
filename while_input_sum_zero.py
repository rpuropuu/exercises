base = []

while True:
    base.append(int(input()))
    if sum(base) == 0:
        break
print(sum([i**2 for i in base]))
