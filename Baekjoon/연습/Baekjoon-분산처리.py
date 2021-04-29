from sys import stdin
input = stdin.readline
T = int(input())
loop = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
for _ in range(T):
    a, b = map(int, input().split())
    a %= 10
    b %= len(loop[a])
    b = b - 1 if b > 0 else len(loop[a])-1
    print(loop[a][b])