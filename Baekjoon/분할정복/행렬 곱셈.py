from sys import stdin
input = stdin.readline
AN, AM = map(int, input().split())
A = []
for _ in range(AN):
    A.append(list(map(int, input().split())))
BN, BM = map(int, input().split())
B = []
for _ in range(BN):
    B.append(list(map(int, input().split())))
answer = [[0 for _ in range(BM)] for _ in range(AN)]
for i in range(AN):
    for j in range(BM):
        answer[i][j] = sum([A[i][k] * B[k][j] for k in range(AM)])
for i in range(len(answer)):
    print(" ".join(map(str,answer[i])))