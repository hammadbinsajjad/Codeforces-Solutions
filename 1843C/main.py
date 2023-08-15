def solve():
    n = int(input().strip())
    s = 0
    while n >= 1:
        # print(n)
        s += n
        if n  % 2 == 0:
            n = n // 2
        else:
            n = (n - 1) // 2
    # print("===")
    print(s)

t = int(input())
for _ in range(t):
    solve()