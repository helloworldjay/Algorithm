def count01(s, n):
    maxlen = 0 # 최대 길이
    length = 0 # 구간 길이
    for i in range(len(s)):
        if s[i] == "1" :
            length += 1
        elif s[i] == "0" and n == 0 :
            return maxlen
        elif s[i] == "0" and n > 0 :
            n -= 1
            length += 1
        if maxlen < length :
            maxlen = length
    return maxlen    

def solution(road, n):
    maxlength = 0
    for i in range(len(road)):
        if count01(road[i:],n) > maxlength :
                maxlength = count01(road[i:],n)
    return maxlength
print(solution("111011110011111011111100011111", 3))