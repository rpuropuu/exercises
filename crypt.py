from itertools import groupby

input_str = input()

groupped_str = groupby(input_str)

result = "".join("".join((elem, str(len(list(grouper))))) for elem, grouper in groupped_str)

print(result)
