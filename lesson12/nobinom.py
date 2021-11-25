n = int(input())
s = [int(input()) for i in range(n)]
print(*[s[i] + s[i + 1] for i in range(n - 1)])
