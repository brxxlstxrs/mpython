lst = [input() for _ in range(int(input()))]
n = len(lst)
res = [' '.join([str(i + 1), str(lst[i].find('кот') + 1)]) for i in range(n) if 'кот' in lst[i]]
print(*res, sep='\n')
