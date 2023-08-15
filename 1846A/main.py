def solve():
    n = int(input())

    c = 0
    for _ in range(n):
        p, l = map(int, input().split())
        if p - l > 0:
            c += 1
    
    print(c)

def main():
    t = int(input())

    for _ in range(t):
        solve()

main()