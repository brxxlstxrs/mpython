cnt = stopwds = 0
s = input()
while len(s) > 6:
    cnt += 1
    if 'forest' in s:
        stopwds += 1
    elif 'lake' in s:
        stopwds += 1
    elif 'mountain' in s:
        stopwds += 1
    s = input()
if stopwds > cnt / 2:
    print('Came.')
else:
    print('Let us move on.')
