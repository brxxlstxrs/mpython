lst = [int(input()) for i in range(int(input()))]
p = int(input())
while lst:
    c = lst.pop(0)
    if p / c in lst:
        print('ДА')
        break
else:
    print('НЕТ')
