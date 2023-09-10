import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

to_debug = True
def solve():
    n, m = inp_list(int)
    a = inp_list(int)

    s = sum(a)
    if n == s:
        same_val = 0
        for v in a:
            same_val += (v*(v + 1) // 2)
        print(f"{same_val} {same_val}")
    else:
        t = [-x for x in a]
        hq.heapify(t)
        max_val = 0
        for _ in range(n):
            mx = abs(hq.heappop(t))
            print(t)
            max_val += mx
            hq.heappush(t, -(mx - 1))

        print(max_val, end=" ")
        hq.heapify(a)

        min_val = 0
        for _ in range(n):
            mn = hq.heappop(a)
            min_val += mn
            if mn - 1 > 0:
                hq.heappush(a, mn - 1)

        print(min_val)


def main():
    t = 1
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def print(x='', end='\n'):
    sys.stdout.write(str(x))
    sys.stdout.write(end)

def debug(*x, end='\n', sep=' '):
    if not to_debug:
        return
    for _x in x:
        sys.stderr.write(str(_x))
        sys.stderr.write(str(sep))
    sys.stderr.write(end)

main()