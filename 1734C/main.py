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
    s = ['1'] + inp_list()

    res = 0
    for i in range(1, n + 1):
        debug(i, end=" ")
        if s[i] == '0':
            s[i] = '2'
            res += i
            for j in range(i*2, n + 1, i):
                if s[j] == '0':
                    s[j] = '2'
                    res += i
                if s[j] == '1':
                    break
        if s[i] == '2':
            for j in range(i*2, n + 1, i):
                if s[j] == '0':
                    s[j] = '2'
                    res += i
                if s[j] == '1':
                    break
        debug(s, res)
    print(res)
            

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