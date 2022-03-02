word = ''
al = []
lst = []
num = []
cnt = 0
flag = 0
n = int(input())
for i in range(n):
    num.append(int(input()))
for i in range(n):
    lst.append(input())
for s in lst:
    base = set()
    for i in range(len(s)):
        count = 1
        tmp = s[:i] + s[i + 1:]
        for j in tmp:
            if s[i] == j:
                count += 1
        base.add((s[i], count))
    base = tuple(base)
    al.append(base)
for i in range(n):
    if flag:
        break
    setup = [k[1] for k in al[i]]
    if num[i] in setup:
        for d in setup:
            if num[i] == d:
                setup.remove(d)
                if num[i] in setup:
                    flag = 1
                    break
        for j in al[i]:
            if num[i] == j[1]:
                word += j[0]
    else:
        flag = 1
if flag:
    print('нечленораздельно')
else:
    print(word)

