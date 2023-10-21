import sys
import operator as op

to_debug = True
def main():
    n, m = inp_list()
    _c = inp_list()

    c = [{}] * n
    for i, v in enumerate(_c):
        c[i] = {"cost":v, "index":i}

    c.sort(key=op.itemgetter("cost"))

    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = inp_list()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    res = 0
    for v in c:
        if v["index"] not in visited:
            res += v["cost"]
            dfs(graph, v["index"])

    print(res)

visited = set()

def dfs(g, n):
    s = []
    push = s.append
    pop = s.pop

    push(n)

    while s:
        cur = pop()

        if cur in visited:
            continue

        visited.add(cur)

        for child in g[cur]:
            push(child)

def input():
    return sys.stdin.readline().strip()
def inp_list():
    return list(map(int, input().split()))

def debug(*x, end="\n", sep=" "):
    if not to_debug:
        return
    for e in x:
        sys.stderr.write(str(e))
        sys.stderr.write(sep)
    sys.stderr.write(end)

main()
