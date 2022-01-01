def clean(line):
    return ''.join(filter(lambda x: x.isalpha(), line)).capitalize()


dict_word = {}
for _ in range(int(input())):
    for key in [clean(line) for line in input().split()]:
        dict_word[key] = dict_word.get(key, 0) - 1

for i, _ in (sorted(dict_word.items(), key = lambda x: x[::-1])):
    print(i)
