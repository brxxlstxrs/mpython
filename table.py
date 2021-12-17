n1, n2 = map(lambda x: range(int(x)), (input(), input()))
tabl = [[input() for _ in n2] for _ in n1]
print(*['\t'.join(i) for i in tabl], sep='\n')
