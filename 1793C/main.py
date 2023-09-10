import sys
def input():
    return sys.stdin.readline().strip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 3:
        print(-1)
        return

    l = 0
    r = n - 1

    cur_max = n
    cur_min = 1

    while l <= r:
        if a[l] == cur_min:
            l += 1
            cur_min += 1
        if a[l] == cur_max:
            l += 1
            cur_max -= 1
        if a[r] == cur_min:
            r -= 1
            cur_min += 1
        if a[r] == cur_max:
            r -= 1
            cur_max -= 1

        if a[l] not in (cur_max, cur_min) and a[r] not in (cur_max, cur_min):
            break
        
    if l <= r:
        print(l + 1, r + 1)
    else:
        print(-1)

t = int(input())
for _ in range(t):
    solve()
