from itertools import combinations

def comparison(a, b, answer):
    cnum = 0
    clength = 0
    maxlen = 0 # 최대길이
    for i in range(len(a)):
        if a[i] != answer[i] and a[i] == b[i] :
            cnum += 1
            clength += 1
        else :
            if clength > maxlen :
                maxlen = clength
            clength = 0
    if clength > maxlen :
        maxlen = clength
    return cnum + (maxlen**2) # 두 사람의 부정행위 가능성 지수 계산

def solution(answer_sheet, sheets):
    ilist = [i for i in range(len(sheets))] 
    clist = list(combinations(ilist,2)) # 비교할 대상들의 idx 쌍 리스트
    maxn = 0 # 부정행위 가능성 지수 최대값
    for i in range(len(clist)):
        n = comparison(sheets[clist[i][0]], sheets[clist[i][1]], answer_sheet)
        if n > maxn :
            maxn = n
    return maxn

print(solution("24551",["24553", "24553", "24553", "24553"]))