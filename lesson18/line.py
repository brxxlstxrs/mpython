def line(s, t):
    s = [float(i) for i in s.split('x')]
    t = [float(i) for i in t.split(';')]
    if s[0] * t[0] + s[1] == t[1]:
        print('True')
    else:
        print('False')

line("1x+6", "1;7")
line("5x-10", "5;-9")
line("0x+7", "3;7")
line("3.5x+0", "2;7")

