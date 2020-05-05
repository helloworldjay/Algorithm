def isCheck(uid, bid):
    if len(uid) != len(bid):
        return False
    for i in range(len(bid)):
        if bid[i] == "*":
            continue
        if bid[i] != uid[i]:
            return False        
    return True
def listCheck(ulist, blist):
    cnt = 0
    # ulist는 combinations의 결과로 길이가 blen인 리스트를 요소로 하는 리스트
    # blist는 banned_id 로 string을 요소로 하는 리스트
    # ulist의 원소를 하나씩 뽑아 후보군을 대조해 본다. 
    # 후보군에서 만족되는 요소값을 계산해 그 개수를 센다. 
    for i in range(len(ulist)):
        idx = [] # 중복을 제거
        for j in range(len(ulist[i])):
            for k in range(len(blist)):
                if isCheck(ulist[i][j], blist[k]) and k not in idx:
                    idx.append(k)
                    print(idx)
                    break
def solution(user_id, banned_id):
    from itertools import combinations
    blen = len(banned_id)
    cand = list(combinations(user_id,blen)) # 후보 리스트
    print(cand)
    return listCheck(cand,banned_id)

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
# 동시에 2개가 되는 경우는 하나로 선택을 해버리면 뒤에 것을 일치 시킬수가 없다. frodo를 *rodo에 일치시키면 fradi도 일치할 방법이 있지만 frodo를 fr*d*에 일치시키면 방법이 사라진다. 
