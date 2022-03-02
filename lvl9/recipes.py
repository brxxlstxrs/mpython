fridge = set()
count = 0
current_r = set()
for i in range(int(input())):
    fridge.add(input())
for i in range(int(input())):
    recipe = input()
    for j in range(n := int(input())):
        if input() in fridge:
            count += 1
        if count == n:
            print(recipe)
    count = 0

