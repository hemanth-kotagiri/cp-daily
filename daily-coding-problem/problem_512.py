# GOOGLE
# You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. 
# You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.

# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

def findMaxFrom(nums, i, currentStepsAvailable):
    max_index = i + 1
    current_max = nums[max_index]

    j = i + 2
    while j < len(nums) and j <= i + currentStepsAvailable:
        if nums[j] > current_max:
            max_index = j
            current_max = nums[j]
        j += 1
    
    return max_index

    # max_index = i + 1
    # current_max = nums[max_index]

    # j = i + 2
    # while j < len(nums) and j <= i + currentStepsAvailable:
    #     if nums[j] > current_max:
    #         current_max = nums[j]
    #         max_index = j
    #     j += 1
    # for j in range(i+1, i + currentStepsAvailable + 1):
    #     if j > len(nums):
    #         return max_index
    #     if nums[j] > current_max:
    #         current_max = nums[j]
    #         max_index = j


def sol(nums):
    i = 0
    while i < len(nums) - 1:
        currentStepsAvailable = nums[i]
        if currentStepsAvailable == 1:
            i += 1
            continue
        temp = findMaxFrom(nums, i, currentStepsAvailable)
        if i == temp - 1:
            return False
        if temp > i: i = temp
    return True

arr = [1, 3, 1, 2, 0, 1] # True
arr2 = [1, 3, 1, 0, 0] # True

# print(sol(arr))
print(sol(arr2))
