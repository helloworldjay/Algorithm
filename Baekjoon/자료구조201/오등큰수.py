from sys import stdin
from collections import Counter

input = stdin.readline
n = int(input())
ngf = [-1 for _ in range(n)]
a = list(map(int, input().strip().split()))
counter_dict = dict(Counter(a))
stack = [0]
for i in range(1, n):
    while stack and counter_dict[a[stack[-1]]] < counter_dict[a[i]]:
        ngf[stack.pop()] = a[i]
    stack.append(i)
print(' '.join(map(str, ngf)))
