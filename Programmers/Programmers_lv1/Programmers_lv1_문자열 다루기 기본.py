def solution(s):
    isCheck = False
    if len(s) == 4 or len(s) == 6 :
        try :
            int(s)
            isCheck = True
        except :
            isCheck = False

    return isCheck

print(solution("122456"))

