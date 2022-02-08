numbers_list = input().split(", ")

int_number_list = []
for number in numbers_list:
    int_number_list.append(int(number))

odd_number = [number for number in int_number_list if number % 2 == 1]

for i in odd_number:
    if i == odd_number[-1]:
        print(i)
    else:
        print(i, end=", ")