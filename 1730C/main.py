import sys
import math
from collections import deque

input = sys.stdin.readline

def solve():
    s = list(map(int, list(input().strip())))
    n = len(s)

    suff_mns = deque()
    cur_min = 8
    for i in range(n -1 , -1, -1):
        if s[i] <= cur_min:
            suff_mns.appendleft(s[i])
            cur_min = s[i]
            s[i] = math.inf

    for el in s:
        if el == math.inf:
            continue
        suff_mns.append(min(el + 1, 9))

    suff_mns = map(str, sorted(suff_mns))
    print("".join(suff_mns))



def main():
    t = int(input())
    for _ in range(t):
        solve()
main()
