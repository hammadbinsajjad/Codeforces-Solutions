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
    l, r = inp_map(int)

    if r <= 3:
        print(-1)
        return

    if l == r and l % 2 == 1:
        i = 2
        while i*i <= r:
            if r % i == 0:
                print(f"{i} {r - i}")
                return
            i += 1
        print(-1)
        return
    
    for i in range(l,r+1):
        if i % 2 == 0 and i != 2:
            print(f"{i // 2} {i // 2}")
            return

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