def solution(n):
    cnt = 0
    k = 0
    while n/(k+1) - k/2 > 0:
        a = n/(k+1) - k/2
        if int(a) == a:
            cnt += 1
        k += 1
    return cnt

print(solution(15))