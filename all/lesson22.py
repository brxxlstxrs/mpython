# Функции с переменным числом аргументов

# Матрица
def matrix(n=0, m=0, a=0):
    if n == 0:
        n = 1
    if m == 0:
        m = n
    return [[a] * m for i in range(n)]
