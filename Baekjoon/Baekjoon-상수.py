#2908번
from sys import stdin
a, b = stdin.readline().strip().split() # 두 수
a = a[::-1]
b = b[::-1]
print(a) if int(a) > int(b) else print(b)