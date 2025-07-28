def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
            
nums = [2,4,9,6,5]
target = 10

result = twoSum(nums, target)
print("Indices:", result)
print("Values:", [nums[result[0]], nums[result[1]]])
    