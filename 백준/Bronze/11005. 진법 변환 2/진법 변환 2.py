N, B = map(int, input().split())

digits = []
while N > 0:
    remainder = N % B
    if remainder < 10:
        digits.append(str(remainder))
    else:
        digits.append(chr(remainder - 10 + ord('A')))  
    N //= B

print(''.join(reversed(digits)))