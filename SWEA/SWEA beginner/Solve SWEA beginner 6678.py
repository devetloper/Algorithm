words =[]
while True:
	word = input()
	if word == "Python":
		words.append(word)
		break
	else:
		words.append(word)

for word in words:
	print(f">> {word.upper()}")