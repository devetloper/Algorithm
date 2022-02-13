T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	n = int(input())
	m = input().split(" ")
	number_list = []
	for i in m:
		if i != "":
			number_list.append(int(i))

	sorted_list = sorted(number_list)

	for i in range(len(sorted_list)):
		if i % 2 == 0:
			sorted_list.insert(i,sorted_list.pop(-1))
	
	sorted_list_10 = sorted_list[:10]
	sorted_list_10 = ' '.join(map(str, sorted_list_10))
	print("#{} {}".format(test_case, sorted_list_10))