# 23분
def solution(N, stages):
    fail_ratio = [0]*(N+1)
    for lv in range(1, N+1):
        # 레벨에 도달한 사람 수, 레벨을 통과한 사람 수
        reached, passed = 0, 0
        for stage in stages:
            if stage > lv :
                passed += 1
            if stage == lv:
                reached += 1    
        fail_ratio[lv] = (reached/(reached+passed)) if reached+passed != 0 else 0
    fail_ratio = sorted(list(enumerate(fail_ratio)), key=lambda x:x[1], reverse=True)
    result = []
    for i in range(len(fail_ratio)):
        if fail_ratio[i][0] != 0:
            result.append(fail_ratio[i][0])
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))