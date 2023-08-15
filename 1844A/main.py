import sys

def input():
    return sys.stdin.readline().strip()

def print(x):
    sys.stdout.write(str(x))
    sys.stdout.write("\n")

def solve():
    a, b = map(int, input().split())
    print(a + b)

def main():
    t = int(input())
    for _ in range(t):
        solve()

main()
