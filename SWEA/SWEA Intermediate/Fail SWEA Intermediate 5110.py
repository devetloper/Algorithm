def put_in(long_list, short_list):
    short_min = min(short_list)
    if short_min >= max(long_list):
        long_list.extend(short_list)
    else:
        i= 0 
        while short_min>= long_list[i]:
            i += 1
        for num in short_list[::-1]:
            long_list.insert(i,num)
    return long_list

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    numbers = []
    for _ in range(m):
        num_list = list(map(int,input().split()))
        numbers.append(num_list)

    ans = numbers[0]
    for i in range(1,n):
        ans = put_in(ans,numbers[i])
    
    ans_10 = ans[-1:-11:-1]
    ans_str= " ".join(list(map(str,ans_10)))
    

    print(f"#{test_case}",ans_str)