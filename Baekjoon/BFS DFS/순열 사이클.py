from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)
def dfs(start, adjacent, visited):
    if visited[start] is False:
        visited[start] = True
        dfs(adjacent[start], adjacent, visited)
for _ in range(int(input())):
    N = int(input())
    adjacent = [0] + list(map(int, input().split()))
    visited = [True] + [False] * (N)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] is False : 
            cnt += 1 
            dfs(i, adjacent, visited)
    print(cnt)

    
    
     