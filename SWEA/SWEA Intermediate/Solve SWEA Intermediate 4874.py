T = int(input())

for test_case in range(1, T + 1):

    str_data = input().split()
    if str_data.index(".") != len(str_data) -1:
        print(f"#{test_case}","error")
    ### stack ###
    stack = []

    def push_item(x):
        stack.append(x)

    def pop_item():
        return stack.pop(-1)


    ### error when number of  int and operator not same ###

    int_data = []
    four_data = []
    for i in str_data:
        try:
            int_data.append(int(i))
        except ValueError:
            four_data.append(i)

    if len(int_data) != len(four_data) :
        print(f'#{test_case}','error')

    ### put str_data into stack ###

    else:
        for i in str_data:
            try:
                push_item(int(i))
            
            except ValueError:

                try:
                    if i != ".":
                        poped_first = pop_item()
                        poped_second = pop_item()
                        
                        if i == "+":
                            push_item(poped_second + poped_first)
                        elif i == "-":
                            push_item(poped_second - poped_first)
                        elif i == "*":
                            push_item(poped_second * poped_first)
                        elif i == "/":
                            push_item(int(poped_second / poped_first))

                    elif i == ".":
                        print(f"#{test_case}",pop_item())

                except IndexError:
                    print(f"#{test_case}","error")
                    