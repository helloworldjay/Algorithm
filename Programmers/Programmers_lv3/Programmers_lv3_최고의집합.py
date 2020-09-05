def solution(n, s):
    if n > s:
        return [-1]
    q, r = divmod(s, n)
    result = [q] * n
    for i in range(1,r+1):
        result[-i] += 1
    return(result)
    