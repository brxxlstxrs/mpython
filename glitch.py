import argparse as ap
from PIL import Image, ImageDraw


def args_init():
    parser = ap.ArgumentParser(description='adds glitch effects to the picture')
    parser.add_argument('input')
    parser.add_argument('-f', '--filter', nargs='?', choices=['lines',], default='lines')
    parser.add_argument('out', nargs='?', default='res.png')
    parser.add_argument('-a', '--addon', nargs='?', default='')
    args = parser.parse_args()
    return args


def opener(inp):
    def decorator(func):
        def wrap(*args, **kw):
            try:
                with Image.open(inp) as im:
                    im.convert('RGB')
                    func(im, *args, **kw)
            except:
                pass
        return wrap
    return decorator


def lines(im, wd=2):
    black = (0, 0, 0)
    w, h = im.size
    draw = ImageDraw.Draw(im)
    for i in range(0, h, wd * 2):
        draw.line(((0, i), (w, i)), fill=black, width=wd)
    return im


def main():
    functs = {'lines': lines}
    args = args_init()
    filt = args.filter
    source, out, addon = args.input, args.out, args.addon
    opn = opener(source)
    print(opn)
    im = opn(filt)(addon)
    print(im)
    im.save(out, 'PNG')
    

if __name__ == '__main__':
    main()

