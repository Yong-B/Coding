N,M = map(int, input().split())
a = []
b = []
i = 0
result = []

for _ in range(N):
    a.append(list(map(int, input().split())))

for _ in range(N):
    b.append(list(map(int, input().split())))

for i in range(N):
    row = []
    for j in range(M):
        row.append(a[i][j] + b[i][j])
    result.append(row)

for r in result:
    print(*r)
    