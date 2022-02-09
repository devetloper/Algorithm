T = int(input())

for test_case in range(1, T + 1):
    numer = int(input())
    numbers_list = input().split(" ")
    int_numbers= []
    for i in numbers_list:
        int_numbers.append(int(i))
        
    max_min = max(int_numbers)-min(int_numbers)
    print(f"#{test_case} {max_min}")