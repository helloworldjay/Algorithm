def majorityElement(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    half = len(nums)//2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])
    print((a, b), [b, a][nums.count(a) > half])
    return [b, a][nums.count(a) > half]

print(majorityElement([1,2,1,3,1,1,1,4]))