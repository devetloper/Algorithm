T = int(input())

for test_case in range(1, T + 1):
	str_data = list(input())

	set_data = sorted(list(set(str_data)))

	in_str = [[] for i in range(len(set_data))]  ### list of letter is in stack or not ###

	### make stack ###
	stack = []
	def push_item(x):
		stack.append(x)

	def pop_item():
		return stack.pop(-1)

	### put str into stack when in_str is empty ###
	def no_repeated(x):
		if len(stack) == 0:
			push_item(x[0])
			return no_repeated(x)
		else:
			for letter in x[1:]:
				poped_item = pop_item()
				if poped_item != letter:
					push_item(poped_item)
					push_item(letter)
				
				else:
					pass
		return len(stack)
			

	print(f"#{test_case}",no_repeated(str_data))

