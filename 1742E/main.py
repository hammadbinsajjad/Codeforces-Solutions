import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

def bsearch(a, v):
    debug(v)
    l = 0
    r = len(a) - 1
    mid = 0
    ind = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= v:
            l = mid + 1
            ind = mid
        else:
            r = mid - 1
        debug(l, r)
    return ind

to_debug = False
def solve():
    n, q = inp_map(int)

    a = inp_list(int)
    s = [a[0]] * n
    h = [a[0]] * n

    for i in range(1, n):
        if a[i] < s[i - 1]:
            s[i] = s[i - 1]
        else:
            s[i] = a[i]
        h[i] = h[i - 1] + a[i]

    debug(a, s, h)

    k = inp_list(int)

    for e in k:
        mid = bsearch(s, e)
        if mid == -1:
            print(0, end=" ")
            continue
        print(h[mid], end=" ")
    print()

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