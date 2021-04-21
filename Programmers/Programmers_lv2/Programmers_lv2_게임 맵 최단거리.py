def solution_bfs(maps):
    from collections import deque
    n, m = len(maps), len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    visiting = deque([(0, 0)])
    visited[0][0] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    while visiting:
        x, y = visiting.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1 and visited[xx][yy] == -1:
                visited[xx][yy] = visited[x][y] + 1
                visiting.append((xx, yy))
    return visited[n-1][m-1]

def solution_dfs(maps):
    from sys import setrecursionlimit
    setrecursionlimit(10**9)
    n, m = len(maps), len(maps[0])
    visited = [[10001 for _ in range(m)] for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    def dfs(x, y, depth):
        visited[x][y] = depth
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 1 and visited[xx][yy] > depth+1:
                dfs(xx, yy, depth+1)
    dfs(0, 0, 1)
    if visited[n-1][m-1] == 10001:
        return -1
    return visited[n-1][m-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))