class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # Brute Force O(N^3) -> 속도 이슈 발생
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0 : result.append([nums[i],nums[j],nums[k]])
        
        # Two Pointer
        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i-1]: continue # 중복제거
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[i] + nums[right] < 0: left += 1
                elif nums[left] + nums[i] + nums[right] > 0: right -= 1
                else : 
                    result.append([nums[i], nums[left], nums[right]]) # 이것으로 연산을 종료하면 while을 빠져나올 방법이 없어 무한루프
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left += 1
                    right -= 1
        
        return result