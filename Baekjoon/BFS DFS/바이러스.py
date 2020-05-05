# 2606번
comp, conn = int(input()), int(input())
clist = [[] for _ in range(comp+1)] # 연결 상태
def dfs(graph, v):
    visited = []
    need_visit = []
    need_visit.append(v) # 시작점 넣기
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
for _ in range(conn):
    s, e = map(int,input().split()) # s 연결 시작, e 연결된 부분
    clist[s].append(e)
    clist[e].append(s)
print(len(dfs(clist,1))-1)










