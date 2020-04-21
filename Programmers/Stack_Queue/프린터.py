
# def solution(priorities, location):
#     idxlist = []
#     cnt = 0 # 프린터 출력 순위
#     start = 0 # 기준점
#     idxlist = [i for i in range(len(priorities))]
#     while True :
#         cnt += 1
#         start = priorities.index(max(priorities))
#         priorities = priorities[start:] + priorities[:start]
#         idxlist = idxlist[start:] + idxlist[:start]
#         if location == idxlist[0]:
#             return cnt
#         else :
#             priorities[0] = 0

# print(solution([1, 1, 9, 1, 1, 1], 0))

# 2배 빠른 다른 사람의 풀이
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans

