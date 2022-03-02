s = [input() for _ in range(int(input()))]
print(', '.join(filter(lambda x: 'лук' not in x, s)))
