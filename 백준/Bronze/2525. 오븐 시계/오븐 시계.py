A, B = map(int, input().split())
C = int(input())
D = (B+C) //60
b = (B+C) % 60
a = (A+D) % 24
print(a,b)