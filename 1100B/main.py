def solve():
    pass
    n= list(map(int,input().strip().split()))[0]
    
    a = list(map(int,input().strip().split()))

    unique_problems = set()

    for i in a:
        if i not in unique_problems:
            unique_problems.add(i)
        if len(unique_problems) == n:
            print(1, end="")
            unique_problems.clear()
        else:
            print(0, end="")

t = 1
for _ in range(t):
    solve()