def twoSum(nums, target):
    indices = []
    for index1 in range(len(nums)-1):
        for index2 in range(index1+1, len(nums)):
            if nums[index1] + nums[index2] == target:
                indices.append(index1)
                indices.append(index2)
                break
        break
    return indices


print(twoSum([3,2,4],6))