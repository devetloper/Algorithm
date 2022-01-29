i=7;k=0
while i>=1:
	if k==0:
		print("*"*i)
		i-=2
		k+=1
	else:
		print(" "*(k-1),"*"*i)
		i -=2
		k+=1


