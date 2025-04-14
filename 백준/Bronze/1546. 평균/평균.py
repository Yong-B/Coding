N = int(input())
scores = list(map(int, input().split()))
max_scores = max(scores)
fake = [(s/max_scores) * 100 for s in scores]
average = sum(fake) / N
print(average)