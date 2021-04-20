from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10**9)
input = stdin.readline
N = int(input())
adj = defaultdict(list)
parents = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)
def find_parent(node):
    adj_list = adj[node]
    visited[node] = True
    for adj_child in adj_list:
        if not visited[adj_child]:
            parents[adj_child] = node
            find_parent(adj_child)
find_parent(1)
print('\n'.join(map(str, parents[2:])))
