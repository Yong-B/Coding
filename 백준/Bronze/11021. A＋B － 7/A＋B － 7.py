T = int(input())
x = 0
for _ in range(T):
    a, b = map(int, input().split())
    x +=1
    print(f"Case #{x}: {a + b}")