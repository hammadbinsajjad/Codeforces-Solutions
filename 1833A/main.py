def solve():
    n = int(input())

    s = input()

    st = set()

    for i, c in enumerate(s[:-1]):
        st.add(s[i] + s[i + 1])

    print(len(st))
    

t = int(input())

for _ in range(t):
    solve()