pi = 3.14159265358979323846264338327950288419716939937510
amount = 0
n = int(input())
for i in range(1, n + 1):
	amount += 1 / (i ** 2)
print((pi ** 2) / amount)