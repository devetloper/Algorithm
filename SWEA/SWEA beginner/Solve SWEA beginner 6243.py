words = input().split()

sorted_words = sorted(words)

not_overlaped_words = []
for word in sorted_words:
	if word not in not_overlaped_words:
		not_overlaped_words.append(word)

for word in not_overlaped_words:
	if word == not_overlaped_words[-1]:
		print(word)
	else:
		print(word, end=",")

