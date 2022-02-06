x,y = map(int,input().split(","))

list_out=[]
for i in range(x):
	list_in =[]
	for j in range(y):
		list_in.append(i * j)
	list_out.append(list_in)

print(list_out)

