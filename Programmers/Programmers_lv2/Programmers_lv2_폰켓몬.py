def solution(nums: list) -> int:
    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    return len(nums)//2 if len(nums)//2 <= len(nums_dict) else len(nums_dict)


print(solution([3,3,3,2,2,2]))
