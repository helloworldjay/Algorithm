from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
partial_sequence = []
visited = [False] * N
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, partial_sequence)))
    else:
        for i in range(N):
            if not visited[i] and (not partial_sequence or partial_sequence[-1] < (i+1)):
                visited[i] = True
                partial_sequence.append(i+1)
                backtracking(depth+1)
                partial_sequence.pop()
                visited[i] = False
backtracking(0)