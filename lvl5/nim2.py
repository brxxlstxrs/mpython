n1 = int(input())
n2 = int(input())
while (n1 != 0) or (n2 != 0):
    num = int(input())
    if num == 1:
        k = int(input())
        n1 -= k
        print(n1, n2)
    elif num == 2:
        f = int(input())
        n2 -= f
        print(n1, n2)
