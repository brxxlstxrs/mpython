n = int(input())
while str(n)[0] == '1' and n < 1e6:
    n *= int(str(n)[0])
print(n)
