# 2606번
from sys import stdin
from collections import deque
c = int(stdin.readline().strip()) # 컴퓨터 대수
l = int(stdin.readline().strip()) # 연결 수
adj = {} # 연결 딕셔너리
for i in range(l):
    s, e = map(int, stdin.readline().strip().split()) # 연결 시작점, 끝점
    if s not in adj:
        adj[s] = [e]
    else :
        adj[s].append(e)
    if e not in adj: # 양방향으로 연결
        adj[e] = [s]
    else:
        adj[e].append(s)
for i in adj: # 번호 순으로 정렬
    adj[i].sort()

def virusdetect(graph) :
    curvirus = deque()
    curvirus.append(1) # 현재 걸린 바이러스
    virushistory = [] # 바이러스 리스트
    while curvirus:
        w = curvirus.popleft()
        if w not in virushistory:
            virushistory.append(w) # 기록에 보관
        if w in graph:
            if w not in virushistory :
                for j in graph[w]:
                    curvirus.append(j)
    return virushistory

print(len(virusdetect(adj)))