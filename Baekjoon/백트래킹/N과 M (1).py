from sys import stdin
from itertools import permutations
input = stdin.readline
n, m = map(int, input().split())
base_list = [str(i) for i in range(1, n+1)]
permutation_list = list(permutations(base_list, m))
for combination in permutation_list:
    print(' '.join(combination))