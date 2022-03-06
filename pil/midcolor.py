from PIL import Image
from statistics import mean

dct = {'r': [], 'g': [], 'b': []}
im = Image.open('image.jpeg')
im.convert('RGB')
pixels = im.load()
x, y = im.size
for i in range(x):
    for j in range(y):
        print(*zip(dct.keys(), pixels[i, j]))
        map(lambda x: dct[x[0]].append(x[1]), list(zip(dct.keys(), pixels[i, j])))
print(*map(mean, dct.values()))

