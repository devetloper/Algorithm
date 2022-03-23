from tempfile import tempdir


nums = [2,7,5,9,3,6,4]

####find max number

#find leaf
n = 1
while  len(nums) > 2 **n -1 :
    n += 1
# print(n) #n = level
cut = 2 ** (n-1) -1
# print(nums[cut:]) #nums[cut:] == leaf

# pump up bigger number to top
for i in range(cut,len(nums)):
    if nums[i] > nums[(i-1) // 2]:
        temp = nums[i]
        nums[i] = nums[(i-1) // 2]
        nums[(i-1) // 2] = temp

print(nums)



