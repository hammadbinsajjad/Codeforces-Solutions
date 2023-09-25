import sys
import math
import bisect as bs
import string as strn
import heapq as hq
import collections as clc
import itertools as it
import operator as op
import copy as cp

def mul(a):
    r = 1
    for e in a:
        r *= e
    return r

to_debug = False
def solve():
    global fact
    s = inp_list()

    blocks = []
    l = 0
    r = 0
    # TODO: Create blocks on consuective numbers
    while r < len(s):
        blocks.append(1)
        r += 1
        while r < len(s) and s[r] == s[l]:
            blocks[-1] += 1
            r += 1
        l = r


    ans1 = (len(s) - len(blocks))
    num_possible_results = mul(blocks)
    removal_from_each_possible_result = math.factorial(ans1)
    ans2 = (num_possible_results * removal_from_each_possible_result) % 998244353

    print(ans1, end=" ")
    print(ans2)

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