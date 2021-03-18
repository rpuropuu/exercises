# вод стркои через пробел
st = [str(i) for i in input().split()] # st = [w.lower() for w in input().split()]

st1 = ['']
le = len(st)-1
i = le
# переводим каждый строковый элемент списка в нижний регистр
for j in range(len(st)):
    st[j] = st[j].lower()
# цикл подсчёта и вывода
while i != -1: # расширяет диапазон для отработки цикла
    if st[i] not in st1:
        print(f'{st[i]} {st.count(st[i])}')
        st1.append(st[i])
    i -= 1 # диапазон отрабатывается в обратном порядке


# другой вариант
s = input().lower().split() # можно сразу при вводе делать
for i in set(s):            # символы мелкими
    print(i, s.count(i))    # работает словарь!

# третий вариант использует словарь
x = [i for i in input().lower().split()]
a = {i:x.count(i)for i in x}
for i,j in a.items():
  print(i,j)
