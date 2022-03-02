# x - где находится клад по координате x
# y - где находится клад по координате y
# x1 - где иы находимся по x
# y1 - где мы находимся по y
x = int(input())
y = int(input())
x1 = 0
y1 = 0
index = 1  # направление 1 это y, а (-1) это x
sign = 1 # 1 в плюс -1 в минус
while x1 != x and y1 != y:
	command = input()
	if command == 'налево'
		index = -index
		sign = -sign
	elif command == 'направо'
		index = -index
	elif command == 'разворот':
		sign = -sign
	else:
		n = int(input())
		if index == 1:
			y1 += n
		else:
			x1 += n
		print(x1, x2)
