# from sys import stdin
# from itertools import permutations
# input = stdin.readline
# n, m = map(int, input().split())
# base_list = [str(i) for i in range(1, n+1)]
# permutation_list = list(permutations(base_list, m))
# for combination in permutation_list:
#     print(' '.join(combination))


from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
sequence_visited = [False] * N
partial_sequence = []
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, partial_sequence)))
    else:
        for i in range(N):
            if not sequence_visited[i]:
                sequence_visited[i] = True
                partial_sequence.append(i+1)
                backtracking(depth+1)
                sequence_visited[i] = False
                partial_sequence.pop()
backtracking(0)

