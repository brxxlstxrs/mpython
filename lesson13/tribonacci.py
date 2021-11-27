lst = [1, 1, 1]
n = int(input())
for i in range(n - 3):
    lst.append(sum(lst[-3:]))
if n < 4:
    lst = lst[:n]
print(lst)
