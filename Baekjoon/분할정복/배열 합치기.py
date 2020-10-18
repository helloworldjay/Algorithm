from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
N_list = list(map(int,input().split()))
M_list = list(map(int,input().split()))
# combined = [] # 합쳐진 리스트
# i, j = 0, 0 # N의 인덱스, M의 인덱스
# while i<N and j<M:
#     if N_list[i] < M_list[j]:
#         combined.append(N_list[i])
#         i += 1
#     else :
#         combined.append(M_list[j])
#         j += 1
# combined += N_list[i:] if j == M else M_list[j:]
combined = N_list + M_list
print(' '.join(list(map(str,sorted(combined)))))


