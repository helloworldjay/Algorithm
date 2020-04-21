from sys import stdin
n , b = int(stdin.readline()), list(map(int, stdin.readline().split()))
for i in range(n):
    print(b[i]*(i+1)-b[i-1]*(i), end=' ')
