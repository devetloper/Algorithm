T = int(input())

for test_case in range(1, T + 1):

	str1 = input()
	str2 = input()

	def find_x_in_y(x,y):
		for i in range(len(y) - len(x) + 1):
			if y[i:i + len(x)] == x:
				x_in_y = 1
				return x_in_y
			else:
				x_in_y = 0
		return x_in_y

	print(f"#{test_case}",find_x_in_y(str1,str2))

