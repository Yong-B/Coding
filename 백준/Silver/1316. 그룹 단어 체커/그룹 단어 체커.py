N = int(input())
count = 0

for _ in range(N):
    word = input()
    used = []
    is_group = True

    for i in range(len(word)):
        if(i>0 and word[i]!= word[i -1]):
            if word[i] in used:
                is_group = False
                break
        used.append(word[i])
    if is_group:
        count += 1

print(count)