import argparse as ap
from PIL import Image, ImageDraw

class Gitch():
    def __init__(self):
        self.functs = {'lines': self.lines}
        args = self.args_init()
        self.filter_func = args.filter
        _source, self.out, self.addon = args.input, args.out, args.addon
        im = self.functs(self.addon)
        im.save(self.out, 'PNG')

    def args_init(self):
        parser = ap.ArgumentParser(description='adds glitch effects to the picture')
        parser.add_argument('input')
        parser.add_argument('-f', '--filter', nargs='?', choices=['lines',], default='lines')
        parser.add_argument('out', nargs='?', default='res.png')
        parser.add_argument('-a', '--addon', nargs='?', default='')
        args = parser.parse_args()
        return args
    
    
    def _opener(self, filename):
        def decorator(func):
            def wrap(*args, **kw):
                try:
                    with Image.open(filename) as im:
                        im.convert('RGB')
                        return func(im, *args, **kw)
                except:
                    pass
            return wrap
        return decorator
    
    
    @_opener(_source)
    def lines(self, im, wd=2):
        black = (0, 0, 0)
        if not wd:
            wd = 2
        w, h = im.size
        draw = ImageDraw.Draw(im)
        for i in range(0, h, wd * 2):
            draw.line(((0, i), (w, i)), fill=black, width=wd)
        return im
    
    
if __name__ == '__main__':
    run = Gitch()

