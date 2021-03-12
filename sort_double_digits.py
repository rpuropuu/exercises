import collections
final_string = ''
a = [str(i) for i in input().split()]
ready_string = ([item for item, count in collections.Counter(a).items() if count > 1])

for i in ready_string:
    final_string += str(i) + ' '

print(final_string)
