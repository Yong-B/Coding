a = list(map(int, input().split())) # 한줄에 여려개 입력 받기
b = [1,1,2,2,2,8]

for i in range(6):
    print(b[i] - a[i], end =' ')