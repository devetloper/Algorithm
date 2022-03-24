### make heap tree , Have to calculate sum of parents

def min_heap(arr):
    h = 1
    while len(arr) > 2**h -1:
        h += 1
    # h = height of tree
    cut = 2**(h-1) -1 
    parents = [i for i in range(cut)]
    parents_reversesd = list(reversed(parents))
    for i in parents_reversesd:
        if (2*i + 2) < len(arr):
            if arr[i] > arr[2*i + 2]:
                temp = arr[i] 
                arr[i] = arr[2*i + 2]
                arr[2*i + 2] = temp
        elif (2*i + 1) < len(arr):
            if arr[i] > arr[2*i + 1]:
                temp = arr[i] 
                arr[i] = arr[2*i + 1]
                arr[2*i + 1] = temp

n = int(input())
nums = list(map(int,input().split()))
heap_nums = []

for num in nums:
    heap_nums.append(num)
    min_heap(heap_nums)

print(heap_nums)
