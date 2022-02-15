T = int(input())

for test_case in range(1, T + 1):

	str_data = input()
	### make stack function ###
	stack = []

	def push(x):
		stack.append(x)

	def pop():
		return stack.pop(-1)
		
	### make parenthesis list ###
	par_data = []

	for letter in str_data:
		if letter == "(" or letter == ")" or letter == "{" or letter == "}":
			par_data.append(letter)
	###count left,right number ###

	if par_data.count("(") != par_data.count(")") or par_data.count("{") != par_data.count("}"):
		print(f"#{test_case}",0)
		
	### push and pop parenthesis to stack ###
	else:
		for par in par_data:
			if par == "{" or par == "(":
				push(par)
			elif par == "}" or par == ")":
				pop_par = pop()
				if  (pop_par == "{" and par == "}") or (pop_par == "(" and par == ")"):
					pass
				else:
					print(f"#{test_case}",0)
					break
		if len(stack) == 0:
			print(f"#{test_case}",1)

