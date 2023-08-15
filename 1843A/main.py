def solve():
    n = int(input())

    arr = list(map(int, input().strip().split()))

    arr.sort()

    l = 0
    r = n - 1

    s = 0
    while l < r:
        s += abs(arr[r] - arr[l])
        r -= 1
        l += 1

    print(s)

t = int((input()))
for _ in range(t):
    solve()