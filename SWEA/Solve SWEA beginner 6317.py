a=[
	3,5,4,1,8,10,2
	]

def find_max_number(x):
	f = a[0]
	for i in a:
		if i >= f:
			f = i
	return f

max_number = find_max_number(a)
print("max{0} => {1}".format(tuple(a),max_number))

