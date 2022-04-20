numbers = []
while True:
	number = list(input())
	if number == ["0"]:
		break
	numbers.append(number)
	
	
for number in numbers:
	if number == number[::-1]:
		print("yes")
	else:
		print("no")

