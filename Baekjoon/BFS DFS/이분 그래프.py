from sys import stdin
from collections import deque
input = stdin.readline
T = int(input())
def BFS(start, adjacent):
    check_color = [0 for i in range(v+1)]
    check_color[1] = 1
    visited = [False for i in range(v+1)]
    visiting = deque([start])
    while visiting:
        node = visiting.popleft()
        if visited[node]: continue # 이미 방문한 노드라면 다음 것으로 간다.
        visited[node] = True
        color = check_color[node] # 현재 노드의 색깔
        temp = adjacent[node] # 다음 연결 리스트를 색칠해야 한다.
        if color == 2: next_color = 1 
        elif color == 1 : next_color = 2
        for i in range(len(temp)):
            if visited[temp[i]] : continue
            if check_color[temp[i]] != 0 and color != next_color: return False
            check_color[temp[i]] = next_color
        visiting.extend(temp)
    return True

for _ in range(T):
    v, e = map(int,input().split()) # v 정점의 개수, e 간선의 개수
    adjacent = {}
    for i in range(1, v+1): adjacent[i] = []
    for i in range(e):
        node1, node2 = map(int,input().split())
        adjacent[node1].append(node2)
        adjacent[node2].append(node1)
    if BFS(1,adjacent):
        print("YES")
    else:
        print("NO")
        
