from math import ceil # ceil 사용

def solution(progresses, speeds):
    anslist = [] # 배포 리스트
    workdays = [ceil((100-a)/b) for a, b in zip(progresses, speeds)] # 개발 소요 일수
    append = anslist.append 
    start = 0
    for end in range(len(workdays)):
        if workdays[start] < workdays[end] :
            append(end-start)
            start = end
    append(len(workdays)-start)
        
    return anslist