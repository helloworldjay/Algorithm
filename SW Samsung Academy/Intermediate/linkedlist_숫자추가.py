T = int(input())
for idx in range(T):
    N, M, L = map(int, input().split())
    N_list = list(map(int, input().split()))
    for _ in range(M):
        i, num = map(int, input().split())
        N_list = N_list[:i] + [num] + N_list[i:]
    print(f"#{idx+1} {N_list[L]}")
        