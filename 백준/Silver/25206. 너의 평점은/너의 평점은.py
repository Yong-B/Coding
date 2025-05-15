total_score = 0     # 학점 × 평점 총합
total_credit = 0    # 학점 총합

for _ in range(20):  # 예: 20과목 입력 받는 경우
    subject, credit_str, rank = input().split()
    credit = float(credit_str)

    if rank == 'P':
        continue  # Pass는 평점 계산 안 함

    if rank == 'A+':
        score = 4.5
    elif rank == 'A0':
        score = 4.0
    elif rank == 'B+':
        score = 3.5
    elif rank == 'B0':
        score = 3.0
    elif rank == 'C+':
        score = 2.5
    elif rank == 'C0':
        score = 2.0
    elif rank == 'D+':
        score = 1.5
    elif rank == 'D0':
        score = 1.0
    elif rank == 'F':
        score = 0.0
    else:
        continue  # 혹시 이상한 입력은 무시

    total_score += credit * score
    total_credit += credit

# 계산 후 출력
if total_credit > 0:
    print(f"{total_score / total_credit:.6f}")
else:
    print("0.000000")