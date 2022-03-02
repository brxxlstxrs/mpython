def equation(a, b):
    x0, y0 = map(float, a.split(';'))
    x1, y1 = map(float, b.split(';'))
    if x0 == x1:
        print(x0)
    elif y0 == y1:
        print(y0)
    else:
        k = (y0 - y1) / (x0 - x1)
        b1 = y1 - k * x1
        print(k, b1)
