def solution(n):
    import math
    x = math.sqrt(n)
    if int(x) == x :
        return int((x+1)**2)
    else :
        return -1

print(solution(121))


