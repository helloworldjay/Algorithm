
def maxSubArray(nums):
    # dp는 nums의 i 번째 요소를 부분 리스트의 가장 오른쪽 항목으로 갖는 리스트들 중 가장 큰 합을 갖는 리스트
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0] 
    for i in range(1, len(nums)):
        # 만약 dp[i-1]이 음수라면 nums[i]에서 새로 출발하는 것이 더 유리하다. 음수를 합하면 어차피 더 작아지므로 dp[i-1]은 더하면 안된다.
        dp[i] = max(0, dp[i-1]) + nums[i] 
        
    return max(dp)
def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()