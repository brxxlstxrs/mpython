import random

ms = input().split()
rzm = input().split()
nnomer = int(input())
n = int(input())
mass_rng = range(*map(lambda x: int(float(x) * 100), ms))
masses = random.sample([i / 100 for i in mass_rng], n)
razmers = random.choices(range(*map(int, rzm)), k=n)
orbita = random.choices(('round', 'hyperbolic', 'parabolic', 'elliptical'), k=n)
nomera = random.sample(range(nnomer * 10000, (nnomer + 1) * 10000), n)
for i in range(n):
    print(f'Meteorite {nomera[i]} has a mass {masses[i]}, ', end='')
    print(f'size {razmers[i]} and moves in a {orbita[i]} orbit.')
