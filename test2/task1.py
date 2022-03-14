import datetime as dt

dat = dt.datetime.strptime(input(), '%d.%m.%Y')
per = dt.timedelta(days=int(input()))
count, n = 0, 0
while True:
    n += 1
    dat += per
    if n % 3 != 0:
        if dat.weekday() != 0:
            print(dat.strftime('%d-%b-%Y'))
            count += 1
    if count == 5:
        break
