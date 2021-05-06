def solution(gems):
    from collections import defaultdict
    target = len(set(gems))
    left, right = 0, 0
    check_dict = defaultdict(int)
    check_dict[gems[left]] = 1
    cache = [0, len(gems) - 1]
    while left < len(gems) and right < len(gems):
        if len(check_dict) == target:
            if right - left < cache[1] - cache[0]:
                cache = [min(left, right), max(left, right)]
            check_dict[gems[left]] -= 1
            if check_dict[gems[left]] <= 0:
                del check_dict[gems[left]]
            left += 1
        else:
            right += 1
            if right < len(gems):
                check_dict[gems[right]] += 1
    return [cache[0] + 1, cache[1] + 1]


def solution2(gems):
    left, right = 0, len(gems) - 1
    target = len(set(gems))
    cache = [left+1, right+1]
    while left <= right:
        is_check = False
        mid = (left + right) // 2
        for i in range(len(gems)-mid+1):
            if len(set(gems[i:i+mid])) == target:
                if cache[1]-cache[0] > mid or (cache[1]-cache[0] == mid and cache[0] > i+1):
                    cache = [i+1, i+mid]
                is_check = True
                break
        if is_check:
            right = mid - 1
        else:
            left = mid + 1
    return cache







print(solution2(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution2(["AA", "AB", "AC", "AA", "AC"]))
