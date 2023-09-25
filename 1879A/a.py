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
    n = inp_int()
    p = []
    for _ in range(n):
        p.append(inp_list(int))
    debug(p)
    t = []
    for i in range(n):
        if p[0][0] <= p[i][0]:
            t.append(p[i][1] - p[0][1])
    debug(t)
    for i in range(1, len(t)):
        if t[i] >= 0:
            print(-1)
            return
    print(p[0][0])

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