n = int(input())
members = [[] for _ in range(201)]
for _ in range(n):
	age, name = input().split()
	members[int(age)].append(name)

for i in range(201):
	if members[i] != []:
		for member in members[i]:
			print(i ,member)
		

