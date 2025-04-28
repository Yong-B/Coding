from collections import Counter

a = input().upper()
counter = Counter(a)

b = counter.most_common()
c = b[0][1]

d = [char for char, cnt in b if cnt == c]
if len(d) > 1:
    print("?")
else:
    print(d[0])
    