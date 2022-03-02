height = int(input())
width = int(input())
s = input()
p = ' '
print(s * width)
for i in range(height - 2):
    print(f'{s}{p * (width - 2)}{s}')
print(s * width)
