T = int(input())

for test_case in range(1, T + 1):
	#####make searching pallindrom in list function#####

	def pallindrome_list(list,n,m):
		for str in list:
			for i in range(n -m + 1):
				if pallindrome(str,i,m) != None:
					return pallindrome(str,i,m)

	####make searching pallindrome in string function###

	def pallindrome(str,start,length):
		split_str = str[start:start + length]
		reversed_str = "".join(list(reversed(split_str)))
		if split_str == reversed_str :
			return split_str

	#####input#####
	n, m = map(int,input().split(" "))

	str_list = []
	for i in range(n):
		list_in = input()
		str_list.append(list_in)

	#####make col list#######
	pre_col_list = list(zip(*str_list))
	col_list = []
	for i in pre_col_list:
		col_list.append("".join(i))
		

	if pallindrome_list(str_list,n,m) != None:
		print(f"#{test_case} {pallindrome_list(str_list,n,m)} ")
	elif pallindrome_list(col_list,n,m) != None:
		print(f"#{test_case} {pallindrome_list(col_list,n,m)} ")

