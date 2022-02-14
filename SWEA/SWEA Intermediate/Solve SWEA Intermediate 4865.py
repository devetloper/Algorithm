T = int(input())

for test_case in range(1, T + 1):
	str1 = input()
	str2 = input()

	### make letter count set ###
	letter_no_repeated = list(set(str1))

	count_dict ={}
	for letter in letter_no_repeated:
		count_dict[letter] = str2.count(letter)

	print(f"#{test_case}",max(count_dict.values()))
		



