from collections import deque
def solution(s):
    l = []
    c = 1
    for i in s[c:-1]:
        temp = []
        if i == "{":
             for j in range(i+1,len(s)):
                 if int(s[i+j])
    return 

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))