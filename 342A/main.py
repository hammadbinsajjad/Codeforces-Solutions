import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp
import pprint

to_debug = True
def solve():
    n = inp_int()

    arr = inp_list(int)

    counts = [0] * 8

    for num in arr:
        counts[num] += 1

    res = []

    nt = n

    i = 0
    while i < n/3:
        if counts[1] and counts[2] and counts[4]:
            res.append("1 2 4")
            counts[1] -= 1
            counts[2] -= 1
            counts[4] -= 1
        elif counts[1] and counts[2] and counts[6]:
            res.append("1 2 6")
            counts[1] -= 1
            counts[2] -= 1
            counts[6] -= 1
        elif counts[1] and counts[3] and counts[6]:
            res.append("1 3 6")
            counts[1] -= 1
            counts[3] -= 1
            counts[6] -= 1
        else:
            debug("W")
            print(-1)
            return
        nt -= 3
        i += 1

    if nt:
        debug("NT")
        print(-1)
        return
        
    for r in res:
        print(r)
              

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