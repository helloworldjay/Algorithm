# SW 마에스트로 2차 1번 문제
# # 첫 귤의 당도부터 순차적으로 꺼내며 꺼낸 귤의 바로 다음 귤부터 당도를 더해나가 기존의 합보다 크면 갱신해준다. 
# # 당도의 합을 저장할 리스트
# result = [] 
# ra = result.append
# # 입력을 받는다. n = 귤의 개수, sweet = 당도 리스트
# from sys import stdin
# n, sweet = int(stdin.readline()), list(map(int, stdin.readline().strip().split()))
# # 하나씩 꺼내와서 계산한다. 
# for i in range(n):
#     total = 0 # 합 초기화
#     for j in range(i, n):
#         # i번째 요소부터 더해 나가 최대 합이 더 커지면 갱신해준다.
#         if sum(sweet[i:j+1]) > total :
#             total = sum(sweet[i:j+1])
#     ra(total)
# print(max(result))

# SW 마에스트로 2차 2번 문제
from sys import stdin
n, m = map(int, stdin.readline().strip().split()) # n명 m개의 관계
p = [[]]
pa = p.append
for i in range(n): # 1번부터 n번까지 사람들의 능력치
    x, y = map(int, stdin.readline().split())
    pa([x,y])
r = [[] for i in range(n+1)] # 관계 리스트
for i in range(m):
    m1, m2 = map(int, stdin.readline().split())
    if m1 != m2:
        r[m1].extend([m2])
        r[m2].extend([m1])
t = [] # 팀 리스트
ta = t.append
# DFS로 팀 나누기



# SW 마에스트로 2차 3번 문제
# 시작 시간 s와 끝나는 시간 e를 받아와 리스트로 만들어 다른 요소들을 꺼내와 비교를 한다.
# from sys import stdin
# n = int(stdin.readline())
# # 스킬 시간을 저장
# skills = []
# sa = skills.append
# # 결과 저장
# result = []
# ra = result.append
# # 시작 시간, 끝 시간 입력받기
# for i in range(n):
#     s, e = map(int, stdin.readline().strip().split())
#     sa([s,e])
# # 순차 비교
# for i in range(n):
#     # 비교를 위해 정렬
#     ns = sorted(skills[:i]+skills[i+1:])
#     cnt = 0 # 이기는 사람 수
#     for j in range(n-1):
#         # 순차 정렬에서 s1 < s2 이면 그 이후로는 다 s2보다 크므로 비교 의미가 없다.
#         if ns[j][0] > skills[i][0]:
#             break
#         elif skills[i][0] < ns[j][1]:
#             cnt += 1
#     ra(cnt)
# print('\n'.join(map(str,result)))