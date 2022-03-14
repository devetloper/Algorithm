T = int(input())
for test_case in range(1, T + 1):
	n, m, k = map(int,input().split())
	num_arr = list(map(int,input().split()))



	idx = 0
	for _ in range(k):
		if idx + m < len(num_arr):
			num_arr.insert(idx+m, num_arr[idx+(m-1)] + num_arr[idx+m])
			idx = idx + m
		else:
			if (idx+m) % len(num_arr) == 0 :
				num_arr.append(num_arr[0] + num_arr[-1])
				idx = len(num_arr) -1
			else:
				idx =(idx+m) % len(num_arr)
				num_arr.insert(idx,num_arr[idx]+num_arr[idx-1])
	print(f"#{test_case}", end= " ")
	if len(num_arr) >= 10:
		for i in num_arr[-1:-10:-1]:
			print(i, end= " ")
		print(num_arr[-10])
	else:
		for i in num_arr[-1:0:-1]:
			print(i, end=' ')
		print(num_arr[0])

