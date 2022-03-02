cnt = 0
for i in range(int(input())):
    s = input()
    cnt += 1
    if 'кот' in s:
        print(cnt, s.find('кот') + 1)
