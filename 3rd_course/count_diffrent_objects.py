objects = [1, 2, 1, 2, 3]
ans = 0
cnt = 0
array = []
for obj in objects: # доступная переменная objects
    if obj in array:
        continue
    else:
        ans += 1
        array.append(obj)
print(ans)

# short version
# ans = len(set(objects))
# print(ans)
