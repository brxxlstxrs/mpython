tpl = tuple((input(), input()) for i in range(int(input())))
for i in tpl[::-1]:
    print(i[0], i[1])
