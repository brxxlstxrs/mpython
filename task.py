import sys


def pears_search(pear):
    return len(pear) % 2 == 0 and int(pear) % 10 > int(pear) % 1000 // 100


lst = [i.strip().split('-=-') for i in sys.stdin]
for i in lst:
    print(*filter(pears_search, i), sep='&')
