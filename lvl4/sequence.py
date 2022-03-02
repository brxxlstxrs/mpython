step = 0
n = int(input())
while n > 1:
	if  n % 2:
		n = 3 * n + 1
	else:
		n /= 2
	step += 1
print(step)