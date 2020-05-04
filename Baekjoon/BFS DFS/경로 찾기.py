# BFS
# 11403번
# bfs를 통해 start에서 end로 가는 방법이 있으면 1, 없으면 0으로 한다. 
from collections import deque
def bfs(graph, l, start):
    visited = [0 for _ in range(l)] 
    visiting = deque()
    visiting.append(start)
    while visiting:
        node = visiting.popleft() 
        if visited[node] == 0:
            visited[node] = 1
            visiting.extend(graph[node])
    return visited 

# n = int(input()) # n을 입력
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int, input().split())))
# gp = [] 
# for i in range(n):
#     temp = bfs(matrix[i],n,i)
    
# result = []

print(bfs([[0],[1],[0]],3,0))