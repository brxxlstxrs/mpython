import datetime as dt
from math import pi, sin

birth = dt.datetime.strptime(input(), '%d.%m.%Y')
current = dt.datetime.strptime(input(), '%d.%m.%Y')
t = (current - birth).days
for p in range(23, 34, 5):
    print(round(sin((2 * pi * t) / p) * 100, 2))
