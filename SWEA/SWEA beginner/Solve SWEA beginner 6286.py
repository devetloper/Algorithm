def fibo(x):
	if x == 1:
		return 1
	elif x == 2:
		return 1
	else:
		return fibo(x-2)+fibo(x-1)
fibo_list = [fibo(i) for i in range(1,11)]
print(fibo_list)

