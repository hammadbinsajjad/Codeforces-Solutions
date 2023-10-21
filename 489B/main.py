def inp_list():
    return list(map(int, input().strip().split()))

def solve():
    n = int(input())
    a = sorted(inp_list())

    m = int(input())
    b = sorted(inp_list())

    taken_a = [False] * n
    taken_b = [False] * m

    res = 0
    for i in range(n):
        for j in range(m):
            v = abs(a[i] - b[j])
            if v <= 1 and not taken_a[i] and not taken_b[j]:
                res += 1
                taken_b[j] = True
                taken_a[i] = True
    
    print(res)

solve()