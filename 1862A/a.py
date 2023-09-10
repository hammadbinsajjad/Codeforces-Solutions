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
    n, m = map(int, input().split())
    carpet = []

    for _ in range(n):
        carpet.append(inp_list())

    found = {}
    c = 0
    crs = ['v', 'i', 'k', 'a']

    for i in range(m):
        for j in range(n):
            if crs[c] == carpet[j][i]:
                found[crs[c]] = True
                if c == 3:
                    print("YES")
                    return
                c += 1
                break
    
    print("NO")
                

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