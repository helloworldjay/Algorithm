from sys import stdin
from collections import Counter
input = stdin.readline
N = int(input())
N_dict = Counter(list(map(int, input().split())))
M = int(input())
count = [0 for _ in range(M)]
M_list = list(map(int, input().split()))
for i in range(len(M_list)):
    if M_list[i] in N_dict:
        count[i] = N_dict[M_list[i]]
print(' '.join(map(str, count)))