word = input().lower()
print(max([word.count(i) for i in set(word)]))
