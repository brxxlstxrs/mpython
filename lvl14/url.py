import re
lst = re.split('\?|&|=', input())[1:]
dct = dict(zip(lst[::2], lst[1::2]))
print(dct[input()])
