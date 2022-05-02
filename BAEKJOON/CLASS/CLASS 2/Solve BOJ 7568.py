n = int(input())

heights = []
weights = []
for _ in range(n):
	h, w = map(int,input().split())
	heights.append(h)
	weights.append(w)

rank = [1 for _ in range(n)]
for i in range(n):
	for j in range(n):
		if heights[i] < heights[j] and weights[i] < weights[j]:
			rank[i] += 1

for i in rank[:-1:]:
	print(i, end=" ")
print(rank[-1])

