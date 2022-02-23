T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split(" "))
    numbers = input().split(" ")
    int_numbers= [int(number) for number in numbers if number != ""]

    def out_in(num_list, times):
        for t in range(times):
            num_list.append(num_list.pop(0))
        return num_list[0]

    print(f"#{test_case}",out_in(int_numbers, m))
