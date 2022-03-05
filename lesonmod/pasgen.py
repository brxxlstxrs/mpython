from string import ascii_letters, digits
from random import choices

es = 'lI1oO0'
data = ascii_letters + digits
for i in es:
    data = data.replace(i, '')


def generate_password(m):
    return ''.join(choices(data, k=m))


def main(n, m):
    st = set()
    res = []
    for i in range(n):
        while True:
            passwd = generate_password(m)
            if passwd not in st:
                st.add(passwd)
                break
        res.append(passwd)
    return res


