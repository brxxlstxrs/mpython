from sys import stdin

words, sentences, exsentances = [], [[]], set()


def distribute_words(elem):
    elem = elem.lower()
    match elem[-1]:
        case '.' | '?':
            sentences[0].append(elem[:-1])
            sentences.insert(0, [])
        case '!':
            sentences[0].append(elem[:-1])
            exsentances.update(sentences[0])
            sentences[0].clear()
        case _:
            sentences[0].append(elem)


def filter_words(sentences, banned):
    words = [word for sentence in sentences[1:] for word in sentence]

    res = sorted(set(word for word in words if (
        words.count(word) > 1 and word not in banned)))

    return res


for elem in stdin.read().split():
    distribute_words(elem)

print(*filter_words(sentences, exsentances))
