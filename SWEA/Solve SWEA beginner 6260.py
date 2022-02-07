ord_list = [ord("a"),ord("z"),ord("A"),ord("Z")]
x = input().split()

upper , lower = 0, 0 
for word in x:
	for i in range(len(word)):
		if ord_list[0] <= ord(word[i]) <= ord_list[1]:
			lower += 1
		elif ord_list[2] <= ord(word[i]) <= ord_list[3]:
			upper += 1
	
print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")

