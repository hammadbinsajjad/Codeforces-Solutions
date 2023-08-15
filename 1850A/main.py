def solve():
    n1, n2, n3 = map(int, input().strip().split())

    if (n1 + n2 >= 10) or (n1 + n3 >= 10) or (n2 + n3 >= 10):
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()  

main()