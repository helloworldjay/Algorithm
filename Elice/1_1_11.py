# cnt = 0
# def convertTo1(num):
#     global cnt
#     if num == 1:
#         return cnt
#     elif num % 3 == 0 :
#         cnt += 1
#         convertTo1(num//3)
#     elif num % 2 == 0 :
#         cnt += 1
#         convertTo1(num//2)


def convertTo1(n):
    dp = [0 for _ in range(n+1)]
    # 점화식 : dp[n] = min(dp(n//3)+1, dp(n//2)+1, dp[n-1]+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1  
    
        if i%2 == 0 and dp[i] > dp[i//2] + 1 :
            dp[i] = dp[i//2]+1
            
        if i%3 == 0 and dp[i] > dp[i//3] + 1 :
            dp[i] = dp[i//3] + 1
        
    return dp[n]
        
def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
