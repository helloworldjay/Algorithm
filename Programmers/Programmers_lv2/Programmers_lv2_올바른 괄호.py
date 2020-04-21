# 알고리즘 : )가 나왔을 때 앞에 (의 개수가 더 적으면 잘못됨. 전체 (와 )의 개수가 달라도 잘못됨 

# 1차 실패
# def solution(s):
#     if s.count("(") != s.count(")"):
#         return False
#     else:
#         for i in range(len(s)):
#             if s[i] == ")":
#                 if s[:i].count("(") <= s[:i].count(")"):
#                     return False
                    
#     return True

# 2차 실패 (1차보다 짧지만 더 오래걸림)
# def solution(s):
#     for i in range(len(s)):
#         if s[:i].count("(") < s[:i].count(")"):
#             return False
#     if s.count("(") != s.count(")"):
#         return False
#     return True
                    
# 3차 실패
# def solution(s):
#     if s.count("(") != s.count(")"):
#         return False
#     else:
#         for i in range(len(s)):
#             if s[:i].count("(") < s[:i].count(")"):
#                 return False
                    
#     return True

# 4차 통과
def solution(s):
    cnt = 0
    for i in range(len(s)):
        cnt = cnt + 1 if s[i] == "(" else cnt - 1
        if cnt < 0:
            return False
    if cnt != 0 :
        return False
    return True    

# 5차 통과 (더 짧게)
def solution(s):
    cnt = 0
    for i in range(len(s)):
        cnt = cnt + 1 if s[i] == "(" else cnt - 1
        if cnt < 0:
            return False
    if cnt != 0 :
        return False
    return True