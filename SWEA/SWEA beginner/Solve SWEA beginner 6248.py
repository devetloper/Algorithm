data_str = input()

even_data_str = []
for i in range(0,len(data_str),2):
	even_data_str.append(data_str[i])

joined_even_data_str = "".join(even_data_str)
print(joined_even_data_str)

