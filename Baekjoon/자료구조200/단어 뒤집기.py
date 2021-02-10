from sys import stdin

input = stdin.readline
n = int(input())
for _ in range(n):
    sentence = input().split()
    print(' '.join([s[::-1] for s in sentence]))
