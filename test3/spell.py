from PIL import Image

def hex_to_rgb(s) -> tuple[int]:
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb) -> str:
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"

def remove_spell(file, res, **colors) -> None:
    with Image.open(file) as im:  # открываем исходное изображение
        im = im.rotate(180)  # поворачиваем на 180 градусов 
        width, height = im.size  # длина и высота
        for x in range(width):
            for y in range(height):
                pixel = im.getpixel((x, y))  # получаем птксель с координатами (x, y)
                pixel = rgb_to_hex(pixel)  # переводим цвет в hex формат
                if pixel in colors:  # если этот цвет нужно заменить
                    res_pixel = hex_to_rgb(colors[pixel])  # нужный цвет в rgb
                    im.putpixel((x, y), res_pixel)  # меняем цвет
        im.save(res)  # сохраняем


colors = {
    "#9dd6f3": "#ccf197",
    "#e3bdfa": "#87c6ee",
    "#ec1c24": "#af2cb6",
    "#985a2e": "#0f5682"
}
remove_spell("input.jpg", "up_and_down.png", **colors)

