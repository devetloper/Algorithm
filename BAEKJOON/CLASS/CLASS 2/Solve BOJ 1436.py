n = int(input())

idx = 0
for i in range(2666800):
	if "666" in str(i):
		idx += 1
		if idx == n:
			print(i)
			break

