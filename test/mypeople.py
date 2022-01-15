myown, stgrs, neutr = [], [], []
for i in range(int(input())):
    n = int(input())
    if n % 7 == 0 or n % 11 == 0:
        myown.append(n)
    elif n > 99 and n % 10 % 2 == 0:
        stgrs.append(n)
    elif n < 99 and n % 7 != 0 and n % 11 != 0:
        neutr.append(n)
if not myown:
    myown.append(0)
if not stgrs:
    stgrs.append(0)
if not neutr:
    neutr.append(0)
print(f'My own people ({abs(min(myown))})')
print(f'Strangers ({max(stgrs)})')
print(f'Neutral ({sum(neutr)})')

