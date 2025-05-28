N = int(input())
result = 0
for i in range(1,N):
    totalsum = sum(map(int, str(i)))
    if i + totalsum ==N:
        result = i
        break
print(result)