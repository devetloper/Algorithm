#Run Time Error, Not using backtracking (5/10)
def permute(arr): #get help
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
    n = int(input())
    numbers =[]
    for _ in range(n):
        row = list(map(int,input().split()))
        numbers.append(row)

    per = permute(list(range(n)))

    min = 99**99
    for col in per:
        total = 0
        for i in range(n):
            total += numbers[i][col[i]-1]
        if total < min:
            min = total
    print(f"#{test_case}",min)
