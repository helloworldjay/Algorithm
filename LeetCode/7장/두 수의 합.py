# Leet Code 1
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_dict:
                return [nums_dict[target], i]
            nums_dict[nums[i]] = i

    # two pointer 사용해보기
    def twoPointerSum(self, nums: List[int], target: int) -> List[int]:
        index_num = []
        for index, num in enumerate(nums):
            index_num.append((index, num))
        index_num.sort(key=lambda x: (x[1], x[0]))
        left, right = 0, len(nums) - 1
        while left != right:
            if index_num[left][1] + index_num[right][1] == target:
                return [index_num[left][0], index_num[left][1]]
            elif index_num[left][1] + index_num[right][1] > target:
                right -= 1
            else:
                left -= 1
        return [-1, -1] # in case of no answer