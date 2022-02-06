number = input()

number_list = list(number)

int_number_list =[]
for i in number_list:
	int_number_list.append(int(i))

sum_number = sum(int_number_list)

print(sum_number)

