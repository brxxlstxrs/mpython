n = int(input())
i = 0
for j in range(n):
    for i in range(j, -1, -1):
        print('Осталось секунд:', i)
    print('Пуск', j + 1)

