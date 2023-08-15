import sys

def input():
    return sys.stdin.readline().strip("\r\n")

def print(x):
    sys.stdout.write(str(x))
    sys.stdout.write("\n")

def solve():
    n = int(input())

    a = list(map(int, input().split()))

    prev = None
    max_dist = float("-inf")

    for n in a:
        if prev is None or n >= prev:
            prev = n
        if prev > n:
            max_dist = max(max_dist, prev)

    if n == len(a) and prev == None:
        print(0)
    else:
        print(max_dist if max_dist != float("-inf") else 0)

def main():
    t = int(input())

    for _ in range(t):
        solve()

main()
