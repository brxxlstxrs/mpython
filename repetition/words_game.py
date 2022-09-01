from sys import stdin


def word_is_ok(word: str, source: str):
    for char in word:
        if char in source:
            char_count = source.count(char)
            source = source.replace(char, "") + char * (char_count - 1)
        else:
            return False
    return True


lst = []
source, *words = stdin.read().splitlines()
for word in words:
    if word_is_ok(word, source):
        lst.append(word)

print(len(lst), *lst, sep="\n")
