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
    n = int(input())
    a = inp_list(int)
    b = [a[0]]
    for i in range(1, n):
        if a[i] == a[i - 1]:
            continue

        b.append(a[i])

    if len(b) == 1:
        print(1)
        return

    #debug(b)
    c = 0
    for i in range(1, len(b) - 1):
        #print(i)
        #debug(b)
        if b[i - 1] < b[i] < b[i + 1]:
            continue
        elif b[i - 1] > b[i] > b[i + 1]:
            continue
        else:
            c += 1

    print(c + 2)

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
