import sys

to_debug = True
def solve():
    n = int(input())

    arr = inp_list(int)

    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1


    prev = n
    # print(counts)

    if max(arr) != n:
        print("NO")
        return

    same = False
    for i in range(1, max(arr)):
        if i in counts:
            prev -= counts[i]
            if arr[i] == prev:
                continue
            else:
                print("NO")
                return
        else:
            if arr[i] == prev:
                continue
            else:
                print("NO")
                return

    print("YES")

def main():
    t = int(input())
    for _ in range(t):
        solve()

def input():
    return sys.stdin.readline().strip('\r\n')

def inp_int():
    return int(input())

def inp_list(f=None):
    return list(map(f, input().split())) if f else list(input())

def print(x='', end='\n'):
    sys.stdout.write(str(x))
    sys.stdout.write(end)

def debug(*x, end='\n', sep=' '):
    if not to_debug:
        return
    for _x in x:
        sys.stderr.write(str(_x))
        sys.stderr.write(str(sep))
    sys.stderr.write(end)

main()