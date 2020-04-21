def solution(clothes):
    cnt = []
    clDict = dict(clothes)
    lst = list(clDict.values())
    lst2 = list(set(clDict.values()))
    for i in range(len(lst2)):    
        cnt.append(lst.count(lst2[i]))
    awr = 1
    for i in range(len(cnt)):
        awr *= cnt[i]+1    
    return awr - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))