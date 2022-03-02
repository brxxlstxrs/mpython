herbs = set()
for i in range(int(input())):
    for j in range(int(input())):
        herbs.add(input())
print(*herbs, sep='\n')
