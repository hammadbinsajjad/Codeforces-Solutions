from operator import itemgetter
import math

def solve():
    n, k = list(map(int, input().strip().split()))

    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    a_with_index = [0] * len(a)
    for i, a_i in enumerate(a):
        a_with_index[i] = {"pred": a_i, "index": i, "orig": math.inf}

    a_with_index.sort(key=itemgetter("pred"))

    b.sort()

    for i, b_i in enumerate(b):
        a_with_index[i]["orig"] = b_i

    a_with_index.sort(key=itemgetter("index"))

    for v in a_with_index:
        print(v["orig"], end=" ")
    print()

t = int(input())

for _ in range(t):
    solve()