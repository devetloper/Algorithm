def facto(a):
	f = 1
	for i in range(a):
		f *= (i+1)
	return f
		
def combination(a,b):
	c = 1
	for i in range(b):
		c *= (a-i) 
	return int(c / facto(b))
		
		
n, k = map(int,input().split())

print(combination(n,k))

