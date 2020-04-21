
def solution(s):
    arry = list(s)
    if len(arry) % 2 != 0 :
        return arry[(len(arry)-1)//2]
    else :
        return arry[(len(arry)-1)//2] + arry[(len(arry)-1)//2 + 1]
    
print(solution("abcde"))

