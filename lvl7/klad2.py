x1 = 0
y1 = 0
count = 0
flag = 0
x = int(input())
y = int(input())
while (s := input()) != 'стоп':
    if not(x1 == x and y1 == y) and flag == 0:
        count += 1
    else:
        flag = 1
    n = int(input())
    if s == 'север':
        y1 += n
    elif s == 'юг':
        y1 -= n
    elif s == 'запад':
        x1 -= n
    elif s == 'восток':
        x1 += n
print(count)