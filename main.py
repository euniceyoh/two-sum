# return indices of 2 integers from array "nums" that add up
# to integer "target"

#from ast import List

# create double for loop 
# if sum equals target, return list of indices 
# return -1, -1 
def twoSum(nums, target): 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                #print([i, j])
                return [i, j]
    return [-1,-1]

print(twoSum([2,7,11,15], 9)) # [0,1]
print(twoSum([3,2,4], 6)) #[1,2]
print(twoSum([3,3], 6)) # [0,1]





