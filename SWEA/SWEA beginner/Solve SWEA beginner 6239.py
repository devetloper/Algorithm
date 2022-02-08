data_sentence = input().split()
for i in range(len(data_sentence)):
	if i == len(data_sentence) -1:
		print(data_sentence[-(i +1)])
	else:
		print(data_sentence[-(i +1 )], end= " ")

