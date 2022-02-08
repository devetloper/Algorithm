a=[1,2,3,4,3,2,1]
def no_twice(x):
	a=[]
	for i in x:
		if i not in a:
			a.append(i)
	return a

a_nt=no_twice(a)
print(a)
print(a_nt)

