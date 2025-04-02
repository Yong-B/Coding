N = int(input())  # 입력받기
a = N // 4  # "long"의 개수는 N을 4로 나눈 몫
b = "long " * a  # "long"을 a번 반복
print(b + "int")