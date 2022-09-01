WHAT_BEATS_WHAT = {
    "камень": ("ножницы", "ром"),
    "ножницы": ("бумага", "ром"),
    "бумага": ("камень", "пират"),
    "ром": ("бумага", "пират"),
    "пират": ("ножницы", "камень"),
}


def rock_paper_scissors2(a, b):
    if a == b:
        print("ничья")
    elif a in WHAT_BEATS_WHAT[b]:
        print("второй")
    else:
        print("первый")


a = input()
b = input()
rock_paper_scissors2(a, b)
