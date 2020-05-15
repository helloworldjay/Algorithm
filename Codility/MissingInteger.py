def solution(A):
    setA = sorted(list(set(A)))
    idx = 0
    for i in range(len(setA)):
        if setA[i] > 0:
           idx = i
           break
    setA = setA[idx:]
    start = 1
    for i in range(len(setA)):
        if start != setA[i]:
            return start
        else :
            start += 1
    return len(setA)+1
print(solution([1,1,3,6,4,-2,-3,2,5]) )