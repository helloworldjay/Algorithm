def longestPalindrome(s:str) -> str:
    def expand(left:int, right:int) -> str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        print(s[left+1:right])
        return s[left+1:right]
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s==s[::-1]: return s
    result = ''
    # 기준점을 하나씩 이동시키며 관찰한다.
    for i in range(len(s)-1):
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)
    return result

print(longestPalindrome("babad"))