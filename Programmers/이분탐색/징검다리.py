def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    while left <= right:
        mid = (left + right) // 2
        former_rock = 0
        total_rock = 0
        min_check = 1000000001
        for rock in rocks:
            if rock - former_rock < mid:
                total_rock += 1
            else:
                min_check = min(min_check, rock - former_rock)
                former_rock = rock
        if total_rock > n:
            right = mid - 1
        else:
            answer = min_check
            left = mid + 1
    return answer