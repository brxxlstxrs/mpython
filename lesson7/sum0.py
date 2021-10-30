param = -1
summ = 0
n = int(input())
for i in range(n):
    summ += int(input()) * (param := -param)
print(summ)