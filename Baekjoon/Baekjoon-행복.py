from sys import stdin
# n = int(stdin.readline())
# lst = list(map(int,stdin.readline().split()))
# # # 위에 두줄을 한줄로도 처리 가능
n, lst = int(stdin.readline()), list(map(int, stdin.readline().split()))

print(max(lst)-min(lst))
