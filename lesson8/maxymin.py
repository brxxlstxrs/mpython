b1 = 0
firsttime1 = 1
firsttime2 = 1
bglobal = 0
c = 0
a = 0
b = 0
n = int(input())
for i in range(n):
    c = int(input())
    for j in range(c):
        if firsttime1:
            b = int(input())
            firsttime1 = 0
        a = int(input())
        if a > b:
            b = b
        else:
            b = a            
    firsttime1 = 1
    if firsttime2:
        c = int(input())
        for j in range(c):
            if firsttime1:
                b1 = int(input())
                firsttime1 = 0
            a = int(input())
            if a > b1:
                b = b1
            else:
                b1 = a
        bglobal = b1
        firsttime2 = 0
    if bglobal > b:
        bglobal = b
    else:
        bglobal = bglobal
print(bglobal)
