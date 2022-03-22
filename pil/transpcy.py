from PIL import Image


def transparency(inp1, inp2):
    im1 = Image.open(inp1)
    im2 = Image.open(inp2)
    im1.putalpha(128)
    im2.putalpha(128)
    im1.paste(im2, (0, 0))
    im1.save('res.jpg')
