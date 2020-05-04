def isCheck(uid, bid):
    if len(uid) != len(bid):
        return False
    for i in len(bid):
        if bid[i] == "*":
            continue
        if bid[i] != uid[i]:
            return False        
    return True
def listCheck(ulist, blist):
    cnt = 0
    for i in range(len(ulist)):
        idx = []
        for j in range(len(blist)):
            if isCheck(ulist[i][j], blist[j]) and j not in idx:
                idx.append(j)
        if len(idx) == len(blist):
            cnt +=1
    return cnt
def solution(user_id, banned_id):
    from itertools import combinations
    blen = len(banned_id)
    cand = list(combinations(user_id,blen)) # 후보 리스트
    return listCheck(cand,banned_id)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))