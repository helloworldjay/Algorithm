from sys import stdin
input = stdin.readline
K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]
K_list.sort()
min_len = 0 
max_len = K_list[-1]
mid = max_len
def cutting(K_list, length, N):
    cnt = 0
    for i in range(len(K_list)):
        cnt += (K_list[i]//length)
    if cnt >= N : return True
    return False
while True:
    mid = ((min_len+max_len)//2)
    if max_len == 1:
       print(1) if cutting(K_list, max_len, N) else print(0)
       break
    elif max_len == 0:
        print(0)
        break
    if cutting(K_list, mid, N):
        min_len = mid
    else :
        max_len = mid
    if max_len-min_len <= 1 :
        print(max_len) if cutting(K_list, max_len, N) else print(min_len)
        break

