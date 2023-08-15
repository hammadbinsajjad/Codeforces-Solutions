def solve():
	c = input()
	s = input().strip()
	cl = s[0]
	print(cl,end="")
	reset = False
	for c in s[1:]:
		if reset:
			cl = c
			print(cl,end="")
			reset = False
		else:
			if cl == c:
				reset = True
	print()


t = int(input())
for _ in range(t):
	solve()