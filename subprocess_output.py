# считывает аргументы из консоли, идущие после адреса модуля
# и возвращает принтом эти аргументы в назад в консоль системы:
#> python3 my_solution.py arg1 arg2
#arg1 arg2

import sys
arg_1 = ''
arg_2 = ''
for i in range(1,len(sys.argv)):
    arg_1 = arg_1 + sys.argv[i] + ' '
arg_2 = arg_1
print(arg_2, end=' ')

# альтернативный вариант
import sys
print(*sys.argv[1:])
# альтернативный вариант
import sys
print(' '.join(sys.argv[1:]))
# альтернативный вариант
print(*__import__("sys").argv[1:])
# альтернативный вариант
import sys
print(*sys.argv[1:])
# альтернативный вариант
from sys import argv
print(*argv[1:])
