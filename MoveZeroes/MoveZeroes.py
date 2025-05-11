def moveZeroes(nums:list[int])->None:
    j = 0
    for num in nums:
        if (num !=0):
            nums[j] = num
            j+=1
    for x in range(j,len(nums)):
        nums[x] = 0
    return nums
test_array = [2,3,0,10,0,9]
print(moveZeroes(test_array))
