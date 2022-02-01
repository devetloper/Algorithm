def mult(*nums):
	total=1
	for num in nums:
		if type(num)!=int:
			return "에러발생"
		else:
			total*=num
	return total
		

a=mult(1, 2, '4', 3)
print(a)

