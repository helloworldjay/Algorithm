from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n = int(input()) # 학생들의 수
    n_list = [0] + list(map(int, input().split()))
    in_group = [0]*(n+1)
    group = 1
    for i in range(1, n+1):
        if in_group[i] == 0:
            while in_group[i] == 0 : # 사이클을 만날 때 까지 반복
                in_group[i] = group # 그룹 번호를 부여
                i = n_list[i]
            while in_group[i] == group : # 완성된 사이클을 역순으로 반복
                in_group[i] = -1 # 사이클을 이루면 -1을 할당
                i = n_list[i]
            group += 1
    cnt = 0
    for i in range(1, n+1):
        if in_group[i] > 0 : cnt+=1
    print(cnt)

# 속도 이슈 코드
from sys import stdin
input = stdin.readline
def dfs(start, n_list):
    temp = [start]
    while True:
        check_node = temp[-1]
        target_node = n_list[check_node]
        if target_node == start: # 연결고리가 돌아서 start와 같다면
            for i in range(len(temp)):
                in_group[temp[i]] = True
            break
        elif target_node not in temp:
            temp.append(target_node)
        elif target_node in temp:
            break
for _ in range(int(input())):
    n = int(input()) # 학생들의 수
    n_list = [0] + list(map(int, input().split()))
    in_group = [True] + [False]*(n)
    for i in range(1, n+1):
        if in_group[i] is False:
            dfs(i,n_list)
    print(in_group.count(False))