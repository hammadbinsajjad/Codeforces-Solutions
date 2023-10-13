import sys
import bisect as bs

input = sys.stdin.readline
inp_int = lambda: int(input().strip("\r\n"))
inp_map = lambda f: map(f, input().strip("\r\n").split())
inp_list = lambda f: list(map(f, input().strip("\r\n").split())) if f else list(input().strip("\r\n"))

def bsearch(a, v):
    l = 0
    r = len(a) - 1
    res = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == v:
            return mid
        elif a[mid] > v:
            r = mid - 1
        else:
            l = mid + 1
    return l


def solve():
    n = int(input())
    a = inp_list(int)
    pref = [a[0]] * n
    for i in range(1, n):
        pref[i] = pref[i - 1] + a[i]

    qn = inp_int()
    qrs = inp_list(int)
    for q in qrs:
        ind = bsearch(pref, q)
        print(ind + 1 if ind < n else ind)

solve()
