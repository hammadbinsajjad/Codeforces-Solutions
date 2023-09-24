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
    n = inp_int()
    x = inp_list(int)
    y = inp_list(int)

    a = [(y[i] - x[i]) for i in range(n)]

    a.sort(reverse=True)

    l = 0
    r = n - 1
    c = 0
    while l < r:
        if a[l] + a[r] >= 0:
            l += 1
            r -= 1
            c += 1
        else:
            r -= 1
    print(c)

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