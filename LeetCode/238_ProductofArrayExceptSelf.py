from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        for i in range(len(nums)):
            result.append(temp)
            temp *= nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result

solution = Solution()
solution.productExceptSelf([1,2,3,4])