def solution(n, times):
    slowest, latest = 1, max(times) * n
    sec = 0
    while slowest <= latest:
        mid = (slowest + latest) // 2
        possible_people = 0
        for time in times:
            possible_people += (mid//time)
            if possible_people >= n:
                break
        if possible_people >= n:
            sec = mid
            latest = mid - 1
        else:
            slowest = mid + 1
    return sec

print(solution(6, [7, 10]))