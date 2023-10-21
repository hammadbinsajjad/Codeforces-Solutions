def main():
    n, m, a, b = map(int, input().strip().split())

    if (b / m) >= a:
        print(a*n)
        return
    
    res = 0
    while n > 0:
        if n <= m:
            if a*n < b:
                res += a*n
                n = 0
            else:
                res += b
                n = 0
        else:
            res += b
            n -= m
        # print(res)
    print(res)

main()