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
    arr = inp_list(int)
    res = []
    res.append(arr[0])
    for i in range(1, n):
        if arr[i - 1] <= arr[i]:
            res.append(arr[i])
        else:
            res.append(arr[i])
            res.append(arr[i])
    print(len(res))
    for el in res:
        print(el, end=" ")
    print()

def main():
    t = int(input())
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