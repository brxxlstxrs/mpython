res = []
lst = [int(i) for i in input().split()]
for i in lst:
    dct, b = {}, bin(i)[2:]
    dct['digits'] = len(b)
    dct['units'] = b.count('1')
    dct['zeros'] = b.count('0')
    res.append(dct)
print(res)
