numbers = []
total = 0
for _ in range(10):
    num = int(input())
    total = num % 42
    numbers.append(total)

unique_numbers = set(numbers)

print(len(unique_numbers))
    