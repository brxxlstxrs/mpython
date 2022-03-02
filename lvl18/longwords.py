def print_long_words(text):
    lst = []
    vow = 'аоэиуыеёюяaeiouy'
    for i in text:
        if not(i.isalpha() or i == ' '):
            text = text.replace(i, ' ')
    for w in text.split():
        cnt = 0
        for c in w.lower():
            if c in vow:
                cnt += 1
        if cnt > 3:
            lst.append(w.lower())
    print(*lst, sep='\n')


text = 'Как и в прочих  заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.'
print_long_words(text)
