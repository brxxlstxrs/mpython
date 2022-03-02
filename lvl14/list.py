print(' '.join([str(i ** 2) for i in map(int, (input().split())) if i % 2 != 0 and (i ** 2) % 10 != 9]))
