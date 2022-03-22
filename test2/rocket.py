from PIL import Image, ImageDraw


def rocket(file, color, w):
    im = Image.new('RGB', (16 * w , 24 * w), color[4])
    draw = ImageDraw.Draw(im)
    draw.polygon(((5 * w, 17 * w),
                 (11 * w, 17 * w),
                 (11 * w, 23 * w),
                 (8 * w, 17 * w),
                 (5 * w, 23 * w)), color[0])
    draw.rectangle((int(5.5 * w), 7 * w, int(10.5 * w), 17 * w), color[1])
    draw.polygon(((int(10.5 * w), 7 * w),
                  (int(5.5 * w), 7 * w),
                  (8 * w, w)), color[2])
    draw.ellipse((7 * w, int(8.5 * w), 9 * w, int(10.5 * w)), color[3])
    draw.ellipse((7 * w, 11 * w, 9 * w, 13 * w), color[3])
    draw.ellipse((7 * w, int(13.5 * w), 9 * w, int(15.5 * w)), color[3])
    im.save(file)
    im.show()


col = "#5489FF", "#00F", "#0F0", "#FF0", "#FFF"
rocket("rocket.png", col, 20)

