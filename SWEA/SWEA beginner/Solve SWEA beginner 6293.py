from math import pi

def cir(x):
	return round(2 * int(x) * pi, 2)
	
numbers = input().split(",")
round = [cir(i) for i in numbers]

for i in range(len(round)):
	if i == len(round) - 1:
		print(round[i])
	else:
		print(round[i], end=", ")

