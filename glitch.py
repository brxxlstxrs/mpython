import argparse as ap
from PIL import Image, ImageDraw


def args_init():
    path = 'res.png'
    parser = ap.ArgumentParser(description='adds glitch effects to the picture')
    parser.add_argument('input')
    parser.add_argument('filter', nargs='?', choices=['lines', 'glitch', 'mix'], default='mix')
    parser.add_argument('-o', '--out', nargs='?', default=path)
    parser.add_argument('-w', '--width', type=int, nargs='?', default=5)
    parser.add_argument('-f', '--freespace', type=int, nargs='?', default=3)
    parser.add_argument('-d', '--delta', type=int, nargs='?', default=8)
    args = parser.parse_args()
    return args


def make_image(filename, filter_, *args, **kw):
    with Image.open(filename) as im:
        im.convert('RGB')
        return filter_(im, *args, **kw)


def lines(im, wd, free):
    black = (0, 0, 0)
    w, h = im.size
    draw = ImageDraw.Draw(im)
    for i in range(0, h, free + wd):
        draw.line(((0, i), (w, i)), fill=black, width=wd)
    return im


def glitch(im, delta):
    x, y = im.size
    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels, pixels2 = im.load(), res.load()
    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels[i, j]
                pixels2[i, j] = 0, g, b
            else:
                g, b = pixels[i, j][1:]
                r = pixels[i - delta, j][0]
                pixels2[i, j] = r, g, b
    return res


def main():
    args = args_init()
    source, out = args.input, args.out
    filter_ = args.filter
    width, free, delta = args.width, args.freespace, args.delta
    if filter_ == 'lines':
        im = make_image(source, lines, width, free)
    elif filter_ == 'glitch':
        im = make_image(source, glitch, delta)
    else:
        im = make_image(source, glitch, delta)
        im = lines(im, width, free)
    im.save(out, 'PNG')

if __name__ == '__main__':
    main()

