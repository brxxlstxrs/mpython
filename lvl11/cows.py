first = input()
second = input()
bull = cow = 0
for i in zip(first, second):
    if i[0] == i[1]:
        bull += 1
    elif i[0] in second:
        cow += 1
print(bull, cow)
