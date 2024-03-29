coords = [input().split() for _ in range(int(input()))]
for i in coords:
    if abs(int(i[0])) != abs(int(i[1])) and abs(int(i[0])) > abs(int(i[1])):
        print(f"({i[0]}, {i[1]})")

min_x, max_x, max_y, min_y = [
    min(coords, key=lambda x: int(x[0])),
    max(coords, key=lambda x: int(x[0])),
    max(coords, key=lambda x: int(x[1])),
    min(coords, key=lambda x: int(x[1])),
]
print(
    f"left: ({min_x[0]}, {min_x[-1]})",
    f"right: ({max_x[0]}, {max_x[-1]})",
    f"top: ({max_y[0]}, {max_y[-1]})",
    f"bottom: ({min_y[0]}, {min_y[-1]})",
)
