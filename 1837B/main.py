def solve():
	_ = input()
	s = input().strip()

	import math
	max_v = 1

	temp = 1
	for i in range(1,len(s)):
		if s[i] == s[i - 1]:
			temp += 1
		else:
			temp = 1

		if temp > max_v:
			max_v = temp

	print(max_v + 1)

t = int(input())
for _ in range(t):
	solve()
