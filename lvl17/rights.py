allowed = [input().split('/') for i in range(int(input()))]
for i in range(int(input())):
    s = input().split('/')
    for j in allowed:
        if all(map(lambda x: x[0] == x[1], zip(j, s))):
            if len(j) <= len(s):
                print('YES')
                break
    else:
        print('NO')
