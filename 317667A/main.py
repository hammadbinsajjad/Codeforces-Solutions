import sys
def input():
    return sys.stdin.readline().strip()

def inp_list():
    return list(map(int, input().split()))

def main():
    n, t = inp_list()
    a = [0] + inp_list() + [n]

    for i in range(n):
        a[i] += i

    s = 1
    while s < n + 1:
        if s > t:
            print("NO")
            return
        if s == t:
            print("YES")
            return
        if s < t:
            s = a[s]
    print("NO")

main()
