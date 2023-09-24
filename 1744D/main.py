import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().strip().split()))


    s = 0
    for el in a:
        num_exp_2 = 0
        while el % 2 == 0:
            el //= 2
            num_exp_2 += 1
        s += num_exp_2

    if s >= n:
        print(0)
        return
    else:
        index_bin = []
        for i in range(1, n + 1):
            t = i
            num_exp_2 = 0
            while t % 2 == 0:
                t //= 2
                num_exp_2 += 1
            index_bin.append(num_exp_2)

        index_bin.sort(reverse=True)
        i = 0
        while i < n and s < n:
            s += index_bin[i]
            i += 1

        if s >= n:
            print(i)
        else:
            print(-1)


t = int(input())
for _ in range(t):
    solve()
