count = 0
high = 0
low = 192
while (n := input()) != '!':
	n = int(n)
	if n > 149 and n < 191:
		count += 1
		if n > high:
			high = n
		if n < low:
			low = n
print(count)
print(low, high)
