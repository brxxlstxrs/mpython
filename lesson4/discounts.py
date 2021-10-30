count = 0
while (price := float(input())) > 0:
	if price > 1000:
		price *= 0.95
	count += price
print(count)