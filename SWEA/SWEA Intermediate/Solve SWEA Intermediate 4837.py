
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

	a = [1,2,3,4,5,6,7,8,9,10,11,12]

	num = len(a)

	n, k = map(int,input().split(" "))


	######make bit list ######
	bit_list = [bin(i).lstrip("0b") for i in range(2 ** num)]

	bit_list_num =[]
	for i in bit_list:
		if len(i) < num:
			bit_list_num.append(list("0" * (num- len(i)) + i))
		else:
			bit_list_num.append(list(i))


	####make subset########

	subsets = []
	for i in bit_list_num:
		in_li =[]
		for j in range(num):
			if i[j] == "1":
				in_li.append (a[j])
		subsets.append(in_li)

	####### find total k #######
	total = 0

	for subset in subsets:
		if len(subset) == n:
			if sum(subset) == k:
				total += 1

	print(f"#{test_case} {total}")

