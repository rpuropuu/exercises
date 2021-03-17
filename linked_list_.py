# создаем метод __init__ - инициализирует все поля
# (при создании каждого нового объекта)
# будем приниматься переменную data (сохранять в узле)
# ссылка направления вперёд называется next
# сначала узел ни с чем не связан - устанавливаем next в None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#  метод будет принимать значение, которые мы
# хотим добавить в новый узел (стандартный ключ - self)
    def append(self, val):
        pass

# создаём новый узел с заданным значением
# назовём его end
def append(self, val):
    end = Node(val)
# создаём указатель (поинтер) создаётся ссылка на
# головной элемент списка - head
# мы будем проходить по списку не переназначая в нём ничего
# делаем ссылку на первый узел - self, и сохраняем в n
    n = self

# проходим список до предпоследнего узла
    while (n.next):
        n = n.next

# указываем на последний узел, за которым нет следующего узла
# берём end (новый узел) и устанавливаем n.next = end
    n.next = end

# создаём нвоый объект Node
ll = Node(1)
ll.append(2)
ll.append(3)
#   [1] --> [2] --> [3]

# выведем перый узел и  остальные в цикле while
# fix here pls
node = ll
print(node.data)
while node.next:
    node = node.next
    print(node.data)
