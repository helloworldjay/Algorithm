def solution(gems):
    cache = dict()
    # for i in range(len(gems)):
    #     if gems[i] not in cache:
    #         cache[gems[i]] = 0
    left, right = 0, 0
    cache[gems[left]] = 1
    min_idx = (0,len(gems)-1)
    n = len(list(set(gems)))
    while True:
        # 만약 r이나 l이 구간을 벗어나면 종료
        if left >= len(gems) or right >= len(gems):
            break
        # 만약 이 구간에서 보석이 전부 존재한다면
        # if 0 not in cache.values():
        if n == len(cache):
            # 길이가 최소인지 판단하고 최소라면 현재 길이를 저장해준다.
            if min_idx[1]-min_idx[0] > right - left:
                min_idx = (left, right)
            cache[gems[left]] -= 1
            if cache[gems[left]] == 0 :
                del cache[gems[left]]
            left += 1
        # 보석의 종류가 부족하다면
        else:
            right += 1
            # right에 있는 보석의 count를 1 늘려준다.
            if right < len(gems) : 
                cache[gems[right]] = cache.get(gems[right], 0) + 1
    return (min_idx[0]+1, min_idx[1]+1)
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


# 당연히 효율성에 문제가 있는 코드
# def solution(gems):
#     # 보석의 개수
#     types = len(list(set(gems))) 
#     # 최소 인덱스, 관찰 인덱스
#     start, target = 0, 0
#     min_len = (0, len(gems)-1)
#     # 최소인덱스에서 출발해서 target까지 갔을 때에 요소 수가 같고 가장 짧은 길이보다 더 짧으면 요소 저장 
#     while True:
#         if len(list(set(gems[start:target+1]))) == types and ((min_len[1]-min_len[0]) > (target-start)):
#             min_len = (start,target)
#         target += 1
#         if target == len(gems):
#             start += 1
#             target = start
#         if start == len(gems):
#             break
#     return [min_len[0]+1,min_len[1]+1]

