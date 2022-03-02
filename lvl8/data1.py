n = int(input())
tmp = 9
i = 1
k = 0
while i * tmp < n:
    n -= tmp * i
    i += 1
    tmp = 10 * tmp
if i - 1:
    k = int('9' * (i - 1))
f = n // i + k
print(f)
