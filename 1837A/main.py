def solve():
	x, k = map(int, input().strip().split())

	if x % k != 0:
		print(1)
		print(x)
	else:
		for i in range(1,x):
			if i % k != 0 and (x - i) % k != 0:
				print(2)
				print(i, x - i, sep=" ")
				break

def main():
	t = int(input())
	for _ in range(t):
		solve()

main()