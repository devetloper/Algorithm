x=input()
a=[]
for i in range(10):
	a.append(str(i))
print(" ".join(a))
x_li=list(x)
b=[]
for i in range(10):
	c=x_li.count(str(i))
	b.append(str(c))
print(" ".join(b))


