# 1. lambda함수 활용, 2. sort의 key 조건 활용
def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    return strings

print(solution(["abce", "abcd", "cdx"],2))