def solution(lottos, win_nums):
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    if 0 in lottos_set:
        lottos_set.remove(0)
    cnt_zero = 6 - len(lottos_set)
    candidate = 6 - len(win_nums_set.difference(lottos_set))
    best = 7 - (cnt_zero + candidate) if cnt_zero + candidate > 1 else 6
    worst = 7 - candidate if candidate > 1 else 6
    return [best, worst]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))