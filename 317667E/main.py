import sys

to_debug = True
def main():
    global visited, path
    n, m = inp_list()

    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = inp_list()
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)


    for i in range(n):
        if not dfs(graph, i):
            print("NO")
            return
        path.clear()
    print("YES")


visited = set()
path = []

def dfs(g, n):
    global visited, path

    stack = []
    push = stack.append
    pop = stack.pop

    push(n)

    while stack:
        cur = pop()

        path.append(cur)
        if len(path) >= 3:
            if not hasChild(g, path[-1], path[-3]):
                return False

        if cur in visited:
            continue

        visited.add(cur)

        for ch in g[cur]:
            if ch not in visited:
                push(ch)

    return True

def hasChild(g, a, b):
    for e in g[a]:
        if e == b:
            return True
    return False

def input():
    return sys.stdin.readline().strip()

def inp_list():
    return map(int, input().split())

main()
