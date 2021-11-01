sidea = float(input())
speed = float(input())
counturn = 0
while (sidea - speed) >= 0.01:
    sidea = ((sidea - speed) ** 2 + speed ** 2) ** 0.5
    counturn += 1
print(counturn)