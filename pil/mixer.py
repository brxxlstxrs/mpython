from PIL import Image

def twist_image(inp, out):
    with Image.open(inp) as im:
        w, h = im.size
        res = Image.new('RGB', (w, h))
        left, right = im.crop((0, 0, w // 2, h)), im.crop((w // 2, 0, w, h))
        res.paste(right, (0, 0))
        res.paste(left, (w // 2, 0))
        res.save(out)


twist_image(input(), input())
