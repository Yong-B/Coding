m = []
for _ in range(5):
    row = list(input())
    m.append(row)

max_len = max(len(row) for row in m)
for col in range(max_len):
    for row in range(5):
        if col < len(m[row]):
            print(m[row][col], end ='') 