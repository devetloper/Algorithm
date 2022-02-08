score=[85,65,77,83,75,22,98,88,38,100]

score.sort()
i=score[-1];total=0
while i>=80:
	i=score.pop()
	if i<=80:
		break
	total+=i
print(total)

