lst, j = [input() for _ in range(int(input()))], '\n'.join
for _ in range(int(input())):
    tmp = [lst[int(input()) - 1] for _ in range(int(input()))]
    lst = tmp
print(j(lst))
