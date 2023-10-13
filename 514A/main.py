n = list(map(int, list(input())))
temp = n

for i in range(len(n)):
    if i == 0 and n[i] == 9:
        continue
    if n[i] >= 5:
        n[i] = 9 - n[i]

n = map(str, n)

n = int("".join(n))

print(n)