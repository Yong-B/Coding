N, M = map(int,input().split())
n = int(str(N)[::-1])
m = int(str(M)[::-1])
if n < m:
    print(m)
else:
    print(n)