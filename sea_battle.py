def print_field(field):  # печать поля
    for i in field:
        print(*i, sep='')
    print()


def horizontal_reflect(field):  # отражение по горизонтали
    return [i[::-1] for i in field]


def vertical_reflect(field):  # отражение по вертикали
    return field[::-1]


def transportation(field):  # транспортирование
    return [list(i) for i in zip(*field)]


field = [list('xxx.'),  # исходное поле
         list('....'),
         list('x.xx'),
         list('x...')]
print_field(field)
print_field(horizontal_reflect(field))
print_field(vertical_reflect(field))
print_field(transportation(field))
print_field(horizontal_reflect(vertical_reflect(field)))
print_field(vertical_reflect(transportation(field)))
print_field(transportation(vertical_reflect(field)))
print_field(transportation(vertical_reflect(horizontal_reflect(field))))
