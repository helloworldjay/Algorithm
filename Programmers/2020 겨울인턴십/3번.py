# 3번 30분

def solution(v):
    section = [0,0,0] # 무, 고구마, 감자 구역의 수
    visited = [[0 for i in range(len(v))] for j in range(len(v))]
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    for i in range(len(v)):
        for j in range(len(v)):
            if visited[i][j] == 0 : # 아직 방문을 하지 않았다면
                section[v[i][j]] += 1 # 해당 구역 개수 증가
                visiting = [(i,j)]
                while visiting:
                    x, y = visiting.pop()
                    visited[x][y] = 1 # 방문을 표시
                    for k in range(4):
                        xx, yy = x+dx[k], y+dy[k]
                        if 0<=xx<len(v) and 0<=yy<len(v) and visited[xx][yy] == 0 and v[i][j] == v[xx][yy]:
                            visiting.append((xx,yy))
    return section
print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))