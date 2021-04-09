from sys import stdin
input = stdin.readline
N = int(input())
connection = {}
for _ in range(N):
    A, B = map(int, input().split())
    connection[A] = B
connection_list = sorted(connection.items())
dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if connection_list[j][1] < connection_list[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))