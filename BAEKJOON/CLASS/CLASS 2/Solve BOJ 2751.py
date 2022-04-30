n = int(input())

numbers = []
for _ in range(n):
	numbers.append(int(input()))

numbers = sorted(set(numbers))

for i in numbers:
	print(i)

