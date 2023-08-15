def solve():
    nt = int(input())

    s = list(map(int, input().strip().split()))

    max_count = 0
    count = 0

    for n in s:
        if n == 0:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    
    print(max(max_count,count))

t = int(input())

for _ in range(t):
    solve()