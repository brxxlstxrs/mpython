n = int(input())
amount = 0
iq = 0
for i in range(n):
    iq = int(input())
    if i == 0:
        print(0)
    else:
        if iq > amount / i:
         print('>')
        elif iq < amount / i:
            print('<')
        else:
            print(0)
    amount += iq