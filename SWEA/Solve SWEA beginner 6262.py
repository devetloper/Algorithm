x = input()

str_not_overlap = []
for letter in x:
    if letter not in str_not_overlap:
        str_not_overlap.append(letter)
sorted_str_not_overlap = sorted(str_not_overlap)

count_letter_dic ={}
for letter in sorted_str_not_overlap:
    count_letter_dic[letter] = x.count(letter)

for letter,count in count_letter_dic.items():
    print(f"{letter},{count}")