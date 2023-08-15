from operator import itemgetter
def solve():
    n = int(input())

    res = []

    for i in range(n):
        l, q = map(int, input().strip().split())

        if l <= 10:
            res.append({
                "l":l,
                "q":q,
                "i":i + 1
            })

    res = sorted(res, key=itemgetter("q"),reverse=True)
    print(res[0]["i"])


def main():
    t = int(input())

    for _ in range(t):
        solve()

main()