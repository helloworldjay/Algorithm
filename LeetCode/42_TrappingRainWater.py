from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right = 0, len(height) - 1
        leftmax, rightmax = height[left], height[right]
        water = 0
        while left < right:
            leftmax, rightmax = max(leftmax, height[left]), max(rightmax, height[right])
            if leftmax <= rightmax:
                water += leftmax - height[left]
                left += 1
            else:
                water += rightmax - height[right]
                right -= 1
        return water
