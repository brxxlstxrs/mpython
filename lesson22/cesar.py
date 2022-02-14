sm = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
lr = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encrypt_caesar(msg, shift):
    for i in msg[:]:
        if i in sm:
        	msg += sm[(sm.index(i) + shift) % 32]
        elif i in lr:
            msg += lr[(lr.index(i) + shift) % 32]


masg = input()
encrypt_caesar(masg, int(input()))
print(masg)
