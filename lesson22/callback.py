import datetime


def rplace(s, dat):
    for i in dat:
        if i in s:
            s = s.replace(i, '')
    return s


s, vow = 'bnjkadfbjvbhdyvivdpowqkdkodnh gxbjzncx[pl][lfojgibuyvgytdc]', 'aeiouy'
start_time = datetime.datetime.now()
rplace(s, vow)
print(datetime.datetime.now() - start_time)

start_time = datetime.datetime.now()
''.join(filter(lambda x: x not in vow, s))
print(datetime.datetime.now() - start_time)
