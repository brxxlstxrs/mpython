m = int(input())
n = int(input())
languages = set()
names = set()
for i in range(m + n):
    name = input()
    if name in languages:
        names.add(name)
    else:
        languages.add(name)
d = languages - names
if not d:
    print('NO')
else:
    print(len(d))
