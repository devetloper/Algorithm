a=[]
for i in range(100,301):
	if i%2==0:
		if int(i/10)%2==0:
			if int(i/100)%2==0:
				a.append(i)

for i in a[:-1]:
	print(i,end=",")
print(a[-1])

