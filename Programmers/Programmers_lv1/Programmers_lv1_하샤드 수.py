def solution(x):
    total = sum([int(i) for i in list(str(x))])
    return True if x % total == 0 else False
    
print(solution(12))

