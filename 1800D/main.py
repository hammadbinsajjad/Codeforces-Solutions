results = []

def solve():
    n = int(input())
    string = input()
    count = 0

    for i in range(n - 2):
        if string[i] == string[i + 2]:
            count += 1

    results.append(n - 1 - count)

t = int(input())

for _ in range(t):
    solve()

for r in results:
    print(r)