
T = int(input())

for test_case in range(1, T + 1):
	N = int(input())

	numbers = list(input())

	numbers_no_repeat = []
	for i in numbers:
		if i not in numbers_no_repeat:
			numbers_no_repeat.append(i)


	count_numbers = []
	for i in numbers_no_repeat:
		count_numbers.append((int(i),numbers.count(i)))

	sorted_count = sorted(count_numbers, key = lambda x: x[1], reverse = True)

	max_number = sorted_count[0][1]

	max_list = []
	for i in sorted_count:
		if i[1] == max_number:
			max_list.append(i)
	
	sorted_max_list = sorted(max_list, key = lambda x: x[0], reverse = True)

	print(f"#{test_case} {sorted_max_list[0][0]} {sorted_max_list[0][1]}")


