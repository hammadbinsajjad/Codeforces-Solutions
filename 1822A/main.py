from operator import itemgetter, attrgetter

def get_input():
    return list(map(int, input().strip().split()))

def solve():
    videos = []
    n, t = get_input()
    a = get_input()
    b = get_input()
                
    for i, time in enumerate(a):
        videos.append({"length": time, "entertaining": b[i], "index": i + 1})

    videos = sorted(videos, key=itemgetter("length", "entertaining"), reverse=True)

    for video in videos:
        if video["length"] < t:
            print(video["index"])
            return
    print(-1)

t = int(input())
for _ in range(t):
    solve()