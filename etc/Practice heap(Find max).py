
nums = list(map(int,input().split()))

####find max number

#find leaf
n = 1
while  len(nums) > 2 **n -1 :
    n += 1
# print(n) #n = level
cut = 2 ** (n-1) -1
# print(nums[cut:]) #nums[cut:] == leaf

# pump up bigger number to top
par = list(range(cut))  #node without leaf
par.reverse()

for i in par:
    if (2*i +2) < len(nums): #when node has two children
        if nums[i] < nums[2*i +2] and nums[2*i +1] < nums[2*i +2]:
            temp = nums[i]
            nums[i] = nums[2*i +2]
            nums[2*i +2] = temp
        
        elif nums[i] < nums[2*i +1] and nums[2*i +1] > nums[2*i +2]:
            temp = nums[i]
            nums[i] = nums[2*i +1]
            nums[2*i +1] = temp
    elif (2*i +1) < len(nums): # when node has one child 
        if nums[i] < nums[2*i +1]:
            temp = nums[i]
            nums[i] = nums[2*i +1]
            nums[2*i +1] = temp

    
print(nums[0]) #max number


