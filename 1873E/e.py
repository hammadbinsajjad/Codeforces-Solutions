def trap(height, h):
    s = 0
    for e in height:
        if e < h:
            s += (h - e)
    return s

import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

to_debug = False
def solve():
    n, x = inp_map(int)

    a = [0] + inp_list(int) + [0]

    l = 1
    r = 1e18

    res = 0

    while l <= r:
        mid = (l + r) // 2
        a[0] = mid
        a[-1] = mid
        if trap(a, mid) > x:
            r = mid - 1
        else:
            l = mid + 1
            res = max(res, mid)

    print(int(res))

def main():
    t = int(input())
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_map(f=None):
    return map(f, input().split()) if f else map(int, input().split())

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