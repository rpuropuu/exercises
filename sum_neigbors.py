# нужно вывести строку с перечислением через пробелы, без скобок

input_string = [int(i) for i in input().split()]
ready_string = ''
new_str = []
s_range = len(input_string)
i = 0
for i in range(s_range):
    if s_range == 1:
        new_str = input_string
        break
    if i == 0:
        new_str.append(input_string[s_range - 1] + input_string[1])
    elif i < s_range - 1 and i > 0:
        new_str.append(input_string[i-1] + input_string[i+1])
    else :
        new_str.append(input_string[i-1] + input_string[0])


print(' '.join(map(str, new_str)))  # если список состоит из чисел,
                                    # то придется использовать еще и функцию map.
                                    # То есть вывести элементы списка чисел,
                                    # разделяя их пробелами, можно так.
