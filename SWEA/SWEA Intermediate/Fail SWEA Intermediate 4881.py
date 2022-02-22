### Fail with 5/10 test case (run time error) ###
### Use backtracking, not using permutation ###

### permutaion fuction ###  (get help)
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

T = int(input())
for test_case in range(1, T + 1):

    ### input ###
    n = int(input())

    board = []
    for i in range(n):
        row_str = input().split(" ")
        row = []
        for j in row_str:
            row.append(int(j))
        board.append(row)

    ### make permutation ###
    numbers = permute(list(range(n)))

    ### find case ###
    cases = []
    for cols in numbers:
        case=[]
        for i,col in enumerate(cols):
            case.append([i,col])
        cases.append(case)

    sums = []
    for case in cases:
        case_cord = []
        for cord in case:
            x,y = cord
            case_cord.append(board[x][y])
        case_sum = sum(case_cord)
        sums.append(case_sum)
    print(f"#{test_case}",min(sums))
    

    