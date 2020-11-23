# 풀이 1
# def solution(nums:list, target:int) -> list:
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# 풀이 2
# def solution(nums:list, target:int) -> list:
#     for i, val in enumerate(nums):
#         complement = target - val
#         if complement in nums[i+1:]:
#             return i, nums[i+1:].index(complement) + (i+1) 
#             # nums에서 전체 검색을 하는 index가 아니라 찾은 곳에서 index를 찾고 다시 i+1을 더함

# 풀이 3
# def solution(nums:list, target:int) -> list:
#     nums_maps = {}
#     for i, val in enumerate(nums):
#         nums_maps[val] = i
#     for i, val in enumerate(nums):
#         if target-val in nums_maps and i != nums_maps[target-val]:
#             return i, nums_maps[target-val]

# 풀이 4
def solution(nums:list, target:int) -> list:
    nums_map = {}
    for i, val in enumerate(nums):
        if target-val in nums_map:
            return [nums_map[target-val], i] 
            # 이미 존재한다는 것은 더 작다는 의미이므로 i가 뒤에 나온다.
        nums_map[val] = i

print(solution([2,7,11,15], 9))