from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_num = 0
        for i in range(len(nums)):
            if i%2==0:
                max_num += nums[i]
        return max_num