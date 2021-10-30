lines = 0
l = -1
count = 1
while (s := input()) != 'СТОП':
    if 'кот' in s.lower() and l == -1:
        l = count
        lines += 1
    elif 'кот' in s.lower():
        lines += 1
    count += 1
print(lines, l)