def findPrevWhichMakesEven(a, indx, v):
    for i in range(indx):
        if (v - a[i]) % 2 == 0:
            return True
    return False

def findPrevWhichMakesOdd(a, indx, v):
    for i in range(indx):
        if (v - a[i]) % 2 != 0:
            return True
    return False

def solve():
    n = int(input())

    a = list(map(int, input().strip().split()))

    a.sort()

    # For Even
    if a[0] % 2 == 0:
        for i, a_i in enumerate(a):
            if a_i % 2 == 0:
                continue
            else:
                if findPrevWhichMakesEven(a, i, a_i):
                    continue
                else:
                    print("NO")
                    return
        print("YES")
    else:
        for i, a_i in enumerate(a):
            if a_i % 2 != 0:
                continue
            else:
                if findPrevWhichMakesOdd(a, i, a_i):
                    continue
                else:
                    print("NO")
                    return
        print("YES")



t = int(input())

for _ in range(t):
    solve()