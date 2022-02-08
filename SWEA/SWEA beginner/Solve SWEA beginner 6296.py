a = input().split(", ")

def convert_to_number(x):
	
	number_list=[]
	for i in x:
		number_list.append(str(ord(i)))
	
	float_list = "".join(number_list)
	
	int_number = int(float_list)
	
	len_float = len(float_list)
	
	float_number = 0.1 ** len_float *int_number * (10 **len(number_list[0]))
	
	return (float_number)

words={}
for i in a:
	words[i] = convert_to_number(i)

sorted_words = sorted(words.items(), key = lambda item: item[1])


for word in sorted_words:
	if word == sorted_words[-1]:
		print(word[0])
	else:
		print(word[0], end=", ")

