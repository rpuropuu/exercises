# первый вариант
def modify_list1(l):
    # ищем В массиве, а не В range(l[])
    for x in l[:]:
        if x % 2 == 0:
            l.append(x//2)
        l.remove(x


# второй вариант
# тоже самое в одну строчку
def modify_list2(l):
    l[:] = [i//2 for i in l if not i % 2]

# третий вариант
def modify_list3(l):
    le = len(l)-1
    i = le
    while i!=-1: # расширяет диапазон для отработки цикла
        if l[i]%2:
            del l[i]
        else:
            l[i]=l[i]//2
        i -= 1 # диапазон отрабатывается в обратном порядке
    return


# четвёртый вариант
def modify_list4(l):
    b = []
    for x in l:
        if x % 2 == 0:
            b.append(x // 2)
    l[:] = b # рабочий обман проверки

