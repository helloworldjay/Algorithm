# 2523번
from sys import stdin
n = int(stdin.readline())
for i in range(1, 2*n):
    print("*"*i) if i <= n else print("*"*(2*n-i))