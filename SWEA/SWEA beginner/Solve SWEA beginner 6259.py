ord_list = [ord("a"),ord("z"),ord("A"),ord("Z")]
x = input().split()

digit , letter = 0, 0 
for word in x:
	for i in range(len(word)):
		if ord("0") <= ord(word[i]) <= ord("9"):
			digit += 1
		elif ord_list[0] <= ord(word[i]) <= ord_list[1] or ord_list[2] <= ord(word[i]) <= ord_list[3]:
			letter += 1
	
print(f"LETTERS {letter}")
print(f"DIGITS {digit}")

