arr = []
for _ in range(9):
    row = list(map(int,input().split()))
    arr.append(row)
max_val = -1
row_idx = 0
col_idx = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            row_idx = i
            col_idx = j
print(max_val)
print(row_idx + 1, col_idx + 1)