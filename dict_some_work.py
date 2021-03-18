def update_dictionary(d, key, value):
# првоерка первого условия
    if key in d:
        d[key].append(value)
# проверка второго условия
    elif key is not d:
# обработка исключающих условий
        if 2*key is d:
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key) == None:
            d[2*key] = []
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key) != None:
            d[2*key].append(value)
    return

# битовый сдвиг
def update_dictionary2(d, key, value):
    key <<= key not in d
    d.setdefault(key,[]).append(value) # создаётся ключ без содержания

# сложно
def update_dictionary3(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value] # создаётся ключ без содержания

# присоединения +=
def update_dictionary4(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
