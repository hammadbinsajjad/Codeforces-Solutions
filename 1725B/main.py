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
    n, d = map(int, input().split())

    l = 0
    r = n - 1

    arr = list(map(int, input().split()))
    count = 0
    arr.sort(reverse=True)
    while l <= r:
        mx = arr[l]
        s = mx
        while r > l and s <= d:
            s += mx
            r -= 1
        if s > d:
            count += 1
        l += 1
    print(count)


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