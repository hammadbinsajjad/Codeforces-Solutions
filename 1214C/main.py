import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
seq = deque(input().strip())

if n == 1:
    print("No")
    sys.exit(0)

st = []

push = lambda: st.append("(")
pop = lambda: st.pop()

incorrect = False
while len(seq):
    if seq[0] == '(':
        push()
        seq.popleft()
    else:
        if st:
            pop()
            seq.popleft()
        else:
            if not incorrect:
                seq.popleft()
                seq.append(")")
                incorrect = True
            else:
                print("No")
                sys.exit(0)
    #print(seq)

if len(st) != 0:
    print("No")
else:
    print("Yes")
