import argparse as ap
from PIL import Image, ImageDraw


def lines(inp, out):
    black = (0, 0, 0)
    try:
        with Image.open(inp) as f:
            f.convert('RGB')
            w, h = f.size
            draw = ImageDraw.Draw(f)
            for i in range(0, h, 4):
                draw.line(((0, i), (w, i)), fill=black, width=2)
            f.save(out, 'PNG')
    except:
        pass


def init():
    parser = ap.ArgumentParser(description='adds effects to the picture')
    parser.add_argument('-f', '--filter', nargs='?', choices=['lines',], default='lines')
    parser.add_argument('input')
    parser.add_argument('out', nargs='?', default='res.png')
    args = parser.parse_args()
    return args


def main():
    args = init()
    source = args.input
    globals()[args.filter](args.input, args.out)


if __name__ == '__main__':
    main()

