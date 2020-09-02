# 반복문을 활용
def solution(n):
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    cache[2] = 2
    for i in range(3,n+1):
        cache[i] = (cache[i-1] + cache[i-2])%1000000007
    return cache[n]

# 재귀를 활용
# 프로그래머스 런타임 에러
# 재귀는 깊어질 수록 오버플로우 가능성이 높다.
def solution2(n):
    cache = [0 for _ in range(n+1)]
    if n == 1 or n == 2:
        return n
    if cache[n] != 0 :
        return cache[n]
    cache[n] = (solution(n-1) + solution(n-2))%1000000007
    return cache[n]

print(solution2(10))