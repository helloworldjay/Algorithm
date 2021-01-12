from sys import stdin
input = stdin.readline
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input().strip())
set_n_list = set(n_list)
sorted_set_list = []
for word in set_n_list:
    sorted_set_list.append((len(word), word))
sorted_set_list.sort()
for length, word in sorted_set_list:
    print(word)