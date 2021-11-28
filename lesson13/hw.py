a = ' * \n* *\n***\n* *\n* *'.split('\n')
b = '** \n* *\n** \n* *\n** '.split('\n')
c = ' * \n* *\n*  \n* *\n * '.split('\n')
dct = {'A': a, 'B': b, 'C': c}
out = [dct[i] for i in list(input())]
for i in zip(*out):
    print(*i)
