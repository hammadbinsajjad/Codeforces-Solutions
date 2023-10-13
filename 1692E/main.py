import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp
import queue as q

to_debug = False
def solve():
    n, k = inp_map()
    a = inp_list(int)

    s = sum(a)

    if s < k:
        print(-1)
        return

    left = [(i + 1) for i in range(n) if a[i] == 1]
    right = [(n - i) for i in range(n - 1, -1, -1) if a[i] == 1]

    left_turn = 0
    right_turn = 0

    debug(left)
    debug(right)

    l = 0
    r = 0
    c = 0
    while s > k:
        debug(l, r)
        if left[l] == right[r]:
            if left_turn > right_turn:
                c += left[l] - left_turn
                l += 1
                right.pop()
                left_turn += 1
            else:
                c += right[r] - right_turn
                r += 1
                left.pop()
                right_turn += 1
        elif left[l] < right[r]:
            c += left[l] - left_turn
            l += 1
            right.pop()
            left_turn += 1
        else:
            c += right[r] - right_turn
            r += 1
            left.pop()
            right_turn += 1
        s -= 1
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