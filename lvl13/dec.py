lst = [input() for _ in range(int(input()))]
step = int(input())
for i in range(int(input())):
    del lst[step - 1::step]
print(*lst, sep='\n')
