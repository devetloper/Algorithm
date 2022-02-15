T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	### make factorial function for calculate P###
	def factorial(x):
		total = 1
		for i in range(1,x + 1):
			total *= i
		return total

	### make permutaion function ###	

	# combination(x,y) = xCy
	def combination(x,y):
		return int(factorial(x) / factorial(x-y) / factorial(y))
	### input ###
	n = int(input())
	n = int(n/10)

	### calculate total case ###
	total_case = 0
	for i in range(n//2 +1):
		total_case += (combination(n -i, i) * 2 ** i)

	print(f"#{test_case}",total_case)

