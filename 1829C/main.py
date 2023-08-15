from operator import itemgetter

def solve():
    ...
    t = int(input())

    books = []
    obt_both = False
    for _ in range(t):
        time, skill = list(map(int, input().strip().split()))

        books.append({"time": time, "skill":skill})

    min_time = 2 * 10**6

    for book in books:
        if book["skill"] == 11:
            if book["time"] < min_time:
                min_time = book["time"]
                obt_both = True

    books.sort(key=itemgetter("time"))

    skill1 = False
    skill2 = False

    skill1_time = 0
    skill2_time = 0

    for book in books:
        if book["skill"] == 11:
            continue
        if skill1 and skill2:
            obt_both = True
            break
        if book["skill"] == 10 and not skill1:
            skill1 = True
            skill1_time = book["time"]
        if book["skill"] == 1 and not skill2:
            skill2 = True
            skill2_time = book["time"]

    if obt_both:
        if not skill1_time or not skill2_time:
            print(min_time)
            return

        if min_time < (skill1_time + skill2_time):
            print(min_time)
        else:
            print(skill1_time + skill2_time)
    else:
        if skill1_time and skill2_time:
            if min_time < (skill1_time + skill2_time):
                print(min_time)
            else:
                print(skill1_time + skill2_time)
        else:
            print(-1)

t = int(input())

for _ in range(t):
    solve()