import sys

def input():
    return sys.stdin.readline().strip()

def inp_list():
    return list(map(int, input().split()))

def main():
    global visited, path
    n, m = inp_list()

    graph = [[] for _ in range(n)]

    res = [0] * n

    for _ in range(m):
        l = inp_list()
        count = l[0]
        if count == 0:
            continue

        s = l[1]
        for i in range(2, count + 1):
            graph[s - 1].append(l[i] - 1)
            graph[l[i] - 1].append(s - 1)


    for i in range(n):
        if i in visited:
            continue
        dfs(graph, i)
        count = len(path)
        for e in path:
            res[e] = count

        path.clear()

    for e in res:
        print(e, end=" ")
    print()

visited = set()
path = []

def dfs(g, n):
    global visited, path
    s = []
    push = s.append
    pop = s.pop

    push(n)
    while s:
        cur = pop()

        if cur in visited:
            continue

        visited.add(cur)

        path.append(cur)

        for ch in g[cur]:
            if ch not in visited:
                push(ch)

main()
