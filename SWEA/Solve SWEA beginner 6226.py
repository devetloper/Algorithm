a=[]
for i in range(1,201):
	if i%7==0:
		if i%5!=0:
			a.append(i)
for i in a[:-1]:
	print(i,end=",")
print(a[-1])

