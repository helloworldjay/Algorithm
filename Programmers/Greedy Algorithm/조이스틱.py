# 문제 -> A는 꼭 지나갈 필요가 없어서 A가 나오면 최대한 안 지나가는 방향이 되어야 한다.
def solution(name):
    alphalist = [chr(i) for i in range(65, 91)]
    nlist = list(name)
    total = 0
    for i in range(len(nlist)):
        diff = alphalist.index(nlist[i])
        total += diff if diff <= 13 else (26 - diff)
    verright = 0
    verleft = 0
    if nlist[0] == 'A':
        for l in range(1, nlist):
            if nlist[l] == 'A':
                verright += 1
            else :
                break   
        for m in range(nlist-1, -1, -1):
            if nlist[m] == 'A':
                verleft += 1
            else :
                break
    result = total + len(nlist) - 1 - verright if verright < verleft else total + len(nlist) - 1 - verleft 
    return result
    

print(solution("JAZ"))


# lst = [1,2,3]
# for i in range(len(lst)-1, -1, -1):
#     print(lst[i])