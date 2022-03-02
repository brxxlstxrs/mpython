n = 0
nums = tuple(map(int, input().split()))
a, b = map(int, input().split())
for i in range(a, b + 1):
    n += nums[i]
print(n)

