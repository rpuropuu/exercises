def update_dictionary(d, key, value):
# првоерка первого условия
    if key in d:
        d[key].append(value)
# проверка второго условия
    elif key is not d:
# обработка исключающих условий
        if 2*key is d:
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key)==None:
            d[2*key]=[]
            d[2*key].append(value)
        elif (2*key is not d) and d.get(2*key)!=None:
            d[2*key].append(value)
    return
