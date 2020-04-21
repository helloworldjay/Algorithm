from sys import stdin
from collections import deque

def bfs(graph, v):
    visited = []
    need_visit = deque()
    need_visit.append(v)
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

def dfs(graph, v):
    visited = []
    need_visit = deque()
    need_visit.append(v)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

n, m, start = map(int,stdin.readline().split())
gp = [[] for i in range(n+1)]
rvgp = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int,stdin.readline().split())
    gp[x].append(y)
    gp[y].append(x)
for i in range(n+1):
    rvgp[i] = sorted(gp[i], reverse=True)
    gp[i] = sorted(gp[i])

for i in dfs(rvgp, start):
    print(i, end = ' ')
print()
for i in bfs(gp, start):
    print(i, end=' ')