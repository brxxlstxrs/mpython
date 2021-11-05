flag = 0
n = int(input())
if n == 3:
    print(2)
else:
    if n > 3:
        print(2, 3, sep='\n')
    for i in range(1, n, 2):
        for j in range(2, int(i / 2) + 1):
            if i % j != 0:
                flag = 1
            else:
                flag = 0
                break
        if flag:
            print(i)
    
