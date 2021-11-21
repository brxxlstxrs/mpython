word = ' ' + input() + ' '
while len(word) >= 1:
    print(word := word[1:-1])
