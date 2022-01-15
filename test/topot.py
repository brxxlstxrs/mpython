glasn = 'aeouiy'
lst = []
while (s := input()) != 'FINISH':
    lst.append(s)
words = input().split(', ')
for phrase in set(lst):
    res = set()
    for i in words:
        for j in i.lower():
            if j in glasn and j in phrase.lower():
                res.add(i.lower())
                break
    if res:
        print(phrase, end='++')
        print(*res, sep='_')
