eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
st = set()
s = input()
for i in s:
    if i in eng:
        for j in range(len(eng)):
            if i == eng[j]:
                st.add((i, j + 1))
    elif i in ru:
        for j in range(len(ru)):
            if i == ru[j]:
                st.add((i, j + 1))
print(*st, sep='\n')
