from itertools import permutations
def baseballgame(test,answer):
    s = 0 # strike
    b = 0 # ball
    for i in range(3):
        if test[i] == answer[i]:
            s += 1
        elif test[i] == answer[(i+1)%3] or test[i] == answer[(i+2)%3]:
            b += 1
    return [s,b]
    


def solution(baseball):
    base = ["1","2","3","4","5","6","7","8","9"]
    u = list(permutations(base,3))
    for i in range(len(u)):
        u[i] = ''.join(u[i])
    tempu = u[:]
    for i in range(len(baseball)):
        for j in range(len(u)):
            if baseballgame(str(baseball[i][0]), u[j]) != baseball[i][1:]:
                try:
                    tempu.remove(u[j]) # try except 하지 않으면 list index 오류가 나는 이유는?
                except:
                    pass
    return len(tempu)

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

    
