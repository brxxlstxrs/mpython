cnt = 0
s = input()
for i in range(0, len(s) + 1):
    if 'о' * i in s:
        cnt = i
print(cnt)
