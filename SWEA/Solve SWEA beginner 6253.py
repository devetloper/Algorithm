i=int(input())
b=[]
while i>=1:
	a=i%2
	b.append(str(a))
	i=int(i/2)
di=list(reversed(b))
di_j=int("".join(di))
print(di_j)


