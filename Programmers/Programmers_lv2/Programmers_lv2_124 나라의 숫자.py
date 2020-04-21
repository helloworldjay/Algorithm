def solution(n):
    quota = n//3
    remainder = n%3
    if remainder == 0:
        quota -= 1
    a = solution(quota) if quota != 0 else "" 
    if remainder == 1 or remainder == 2:
        return "{}{}".format(a,remainder)
    elif remainder == 0:
        return "{}{}".format(a,4)

print(solution(3))

    
