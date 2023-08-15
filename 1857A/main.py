import sys
def input():
    return sys.stdin.readline().strip('\r\n')

def print(x="", end=""):
    sys.stdout.write(str(x))
    sys.stdout.write('\n')

def solve():
    _ = input()

    a = list(map(int, input().split()))

    if sum(a) % 2 == 0:
        print("YES")
    else:
        print("NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

main()