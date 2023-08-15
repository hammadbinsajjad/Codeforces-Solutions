results = []

def solve():
    global results
    n, d = list(map(int, input().strip().split()))

    num_s = input().strip()

    # max_num = num_s

    # for i in range(len(num_s) + 1):
    #     num_val = num_s[:i] + str(d) + num_s[i:]
    #     if num_val > max_num:
    #         max_num = num_val

    # results.append(max_num)


    for i, c in enumerate(num_s):
        if int(c) < d:
            results.append(num_s[:i] + str(d) + num_s[i:])
            break
        if i == len(num_s) - 1:
            results.append(num_s + str(d)) 

t = int(input())
for _ in range(t):
    solve()

for r in results:
    print(r)