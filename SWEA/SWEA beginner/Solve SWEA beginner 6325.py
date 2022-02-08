a=[2,4,6,8,10]
def find(x,y):
	return (y in x)
tf_5=find(a,5)
tf_10=find(a,10)
print(a)
print("{0} => {1}".format(5,tf_5))
print("{0} => {1}".format(10,tf_10))

