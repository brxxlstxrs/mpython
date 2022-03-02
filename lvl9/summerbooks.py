m = int(input())
n = int(input())
exists = set()
answers = []
for i in range(m):
    exists.add(input())
for i in range(n):
    s = input()
    if s in exists:
        answers.append('YES')
    else:
        answers.append('NO')
print(*answers, sep='\n')
