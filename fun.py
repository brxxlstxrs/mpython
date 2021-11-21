def subm(line, phrase):
    '''Функция ищет букавы в одной строке текста
        и пишет те которые есть в тексте на тех 
        местах где они встретелись,
        заменяя остальныепробелами'''
    buff = ''
    line, phrase = map(str, [line, phrase])
    phrase = phrase.replace(' ', '')
    for letter in phrase:
        if letter in line:
            n = line.find(letter)
            buff += ' ' * n + line[n]
            line = line[n + 1:]
            phrase = phrase[1:]
    return buff, phrase

def memephrase(phrase, *text):
    buff = ''
    # text = str(text).split('\n')
    for line in text:
        buff += subm(line, phrase)[0] + '\n'
        phrase = subm(line, phrase)[1]
    return buff

text = []
while (line := input()) != '':
    text.append(line)
phrase = input()
print()
print(memephrase(phrase, *text))
