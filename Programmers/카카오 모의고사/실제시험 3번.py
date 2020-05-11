def solution(gems):
    #보석의 종류
    types = list(set(gems))
    minlen = 100000
    result = []
    ck = []
    cnt = 0
    for i in range(len(gems)):
        for j in range(i, len(gems)):
            if gems[i] not in ck :
                ck.append(gems[i])
            if len(ck) == len(types) :
                
                if j-i < minlen :
                    result = [i+1,j+1]
                    minlen = j-i 
    return result

print(solution(["XYZ", "XYZ", "XYZ"]))