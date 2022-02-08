str_data = input()

def make_reverse_str(x):
	reversed_str_data_list = list(reversed(x))

	reversed_str_data = "".join(reversed_str_data_list)

	return reversed_str_data

if make_reverse_str(str_data) == str_data:
	print(make_reverse_str(str_data))
	print("입력하신 단어는 회문(Palindrome)입니다.")

