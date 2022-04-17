str_n = input()
int_n = int(str_n)

if int_n < 18:
	for i in range(1,int_n+1):
		sum = 0
		for j in str(i):
			sum += int(j)
		if i + sum == int_n:
			print(i)
			break
		elif i == int_n:
			print(0)

else:
	for i in range(int_n - len(str_n)*9 ,int_n+1):
		sum = 0
		for j in str(i):
			sum += int(j)
		if i + sum == int_n:
			print(i)
			break
		elif i == int_n:
			print(0)

