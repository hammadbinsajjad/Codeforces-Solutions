def solve():
    s = ""
    for i in range(8):
        si = input().strip(".\n")
        if si:
            s += si
    print(s)

t = int(input())
for _ in range(t):
    solve()