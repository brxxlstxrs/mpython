s = input().lower()
cnt = 0
ch = ''
for i in set(s) - {' '}:
    if s.count(i) > cnt:
        cnt = s.count(i)
        ch = i
    elif s.count(i) == cnt:
        if i < ch:
            ch = i
print(ch)
