def min_heap(arr):
    n = len(arr)-1 
    while n > 0:
        if arr[n] < arr[(n-1)//2]:
            temp = arr[n]
            arr[n] = arr[(n-1)//2]
            arr[(n-1)//2] = temp
        n = (n-1)//2
    
def sum_parent(arr):
    par = int((len(arr)-2)/2)
    total = 0
    while par >= 0:
        total += arr[par]
        if par == 0:
            break
        par = int((par-1)/2)
    return total

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int,input().split()))
    heap_nums = []

    for num in nums:
        heap_nums.append(num)
        min_heap(heap_nums)

    ans = sum_parent(heap_nums)
    print(f"#{test_case}",ans)
