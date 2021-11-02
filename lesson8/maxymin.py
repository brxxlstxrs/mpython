count = 0
flag1 = 1
flag2 = 1
a = 0
b = 0
bglobal = 0
n1 = 0
n = int(input())
for i in range(n):
    n1 = int(input())
    for j in range(n1):
        a = int(input())
        if flag1:
            b = a
            flag1 = 0
        if a < b:
            b = a
    flag1 = 1
    if flag2:
        bglobal = b
        flag2 = 0
    if bglobal < b:
        bglobal = b
        count = i + 1
print(count, bglobal)
