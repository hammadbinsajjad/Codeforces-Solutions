def solve():
    st = input().strip()

    ori = "codeforces"

    count = 0
    for i in range(len(ori)):
        if ori[i] != st[i]:
            count += 1
    
    print(count)

t = int(input())
for _ in range(t):
    solve()