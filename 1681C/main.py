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
    a = inp_list(int)
    b = inp_list(int)

    arr = [(a[i], b[i]) for i in range(n)]

    moves = []

    for i in range(n):
        for j in range(i, n):
            if arr[i][0] > arr[j][0]:
                arr[i], arr[j] = arr[j], arr[i]
                moves.append((i, j))
            elif arr[i][0] == arr[j][0]:
                if arr[i][1] > arr[j][1]:
                    arr[i], arr[j] = arr[j], arr[i]
                    moves.append((i, j))

    res = True
    for i in range(1, n):
        if arr[i][1] < arr[i - 1][1]:
            res = False
            break
    
    if not res:
        print(-1)
    else:
        print(len(moves))
        for p in moves:
            print(p[0] + 1, end=" ")
            print(p[1] + 1)


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