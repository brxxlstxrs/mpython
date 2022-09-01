def answer(lst: list, name: str) -> str:
    ind = lst.index(name)
    return ' -> '.join(lst[(ind - 1 if ind - 1 >= 0 else 0):ind + 2])


lst = input().split(' -> ')
n = int(input())
for i in range(n):
    name = input()
    print(answer(lst, name))
