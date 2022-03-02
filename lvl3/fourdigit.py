n = int(input())
a = n % 10
b = n % 100 // 10
c = n // 100 % 10
d = n // 1000
if a > b:
    a, b = b, a 
if b > c:
    b, c = c, b 
if c > d:
    c, d = d, c 
if a > b:
    a, b = b, a 
if b > c:
    b, c = c, b 
if a > b:
    a, b = b, a 
if a == 0 and b:
    a, b = b, a 
elif a == 0 and b == 0 and c:
    a, c = c, a
elif a == 0 and b == 0 and c == 0:
    a, d = d, a
print(int(str(a) + str(b) + str(c) + str(d)))