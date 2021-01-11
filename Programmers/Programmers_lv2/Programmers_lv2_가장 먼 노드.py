import collections


def check_distance(start, visited, adj):
    cnt = 0
    visiting = collections.deque([[start, cnt]])
    while visiting:
        node, count = visiting.popleft()
        if visited[node] == -1:
            count += 1
            visited[node] = count
            for next in adj[node]:
                visiting.append([next, count])


def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    visited = [-1 for _ in range(n + 1)]
    for start, end in edge:
        adj[start].append(end)
        adj[end].append(start)
    check_distance(1, visited, adj)
    cnt = 0
    for i in range(2, len(visited)):
        if visited[i] == max(visited):
            cnt += 1
    return cnt


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
