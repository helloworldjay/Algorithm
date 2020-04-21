from itertools import combinations 
def solution(numbers, target):
    idxlist = [i for i in range(len(numbers))] # idx 리스트
    collist = []
    coapp = collist.append
    for i in range(1,len(idxlist)+1):
        templist = list(combinations(idxlist,i))
        for j in range(len(templist)):
            coapp(templist[j])
    
    cnt = 0 # 방법 가지수
    for i in range(len(collist)):
        pls = 0 # 더하기 요소
        for j in collist[i]:
            pls += numbers[j]
        if 2*pls - sum(numbers) == target :
            cnt += 1
    return cnt
print(solution([1,1,1,1,1],3))