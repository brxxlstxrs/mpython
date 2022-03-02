st = set()
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for i in range(0, n - 2):
    for j in range(0, n - 2):
        st.add(sum((
            *matrix[i][j:j + 3:2],
            *matrix[i + 1][j:j + 3],
            *matrix[i + 2][j:j + 3:2]
            )))
print(max(st))
