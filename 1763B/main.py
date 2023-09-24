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
    n, k = inp_map(int)

    h = inp_list(int)
    p = inp_list(int)

    m = [{"health": h[i], "power":p[i]} for i in range(n)]

    m.sort(key=op.itemgetter("health"))

    mins = [1e10] * (n + 1)

    for i in range(n - 1, -1, -1):
        mins[i] = min(mins[i + 1], m[i]["power"])

    alive = 0
    dd = 0
    while alive < n and k > 0:
        dd += k

        while alive < n and m[alive]["health"] <= dd:
            alive += 1
        
        k -= mins[alive]

    if alive == n:
        print("YES")
    else:
        print("NO")

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