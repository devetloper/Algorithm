def room(k,n):
	if  memo[k][n-1]:
		return memo[k][n-1]
	else:
		if k ==0:
			return n
		else:
			sum = 0
			for i in range(1,n+1):
				sum += room(k-1,i)
				memo[k][n-1] = sum
		return sum

Tc = int(input())
for _ in range(Tc):
	k = int(input())
	n= int(input())
	memo = [[0 for _ in range(n)] for _ in range(k+1)]
	print(room(k,n))

