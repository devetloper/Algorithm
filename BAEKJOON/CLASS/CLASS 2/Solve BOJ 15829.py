n = int(input())
str = list(input())

numbers = []
for alp in str:
	numbers.append(ord(alp)-96)

hash = 0
for i in range(n):
	hash +=numbers[i] * (31 ** i)

print(hash % 1234567891)

