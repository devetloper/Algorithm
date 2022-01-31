x=list(map(int,input().split(", ")))
def square(x):
	return x**2
for i in x:
	print("square({0}) => {1}".format(i,square(i)))

