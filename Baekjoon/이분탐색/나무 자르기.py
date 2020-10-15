from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
top = 0 # 나무 길이중 최대값
for i in range(N):
    if N_list[i] > top : top = N_list[i]
bot = 0 # 아래 기준선
def cutting(check):
    length = 0 # 얻을 수 있는 나뭇가지의 길이
    for i in range(N):
        if N_list[i] > check: length += (N_list[i]-check)
    if length >= M: return True
    return False
while top >= bot:
    mid = (top+bot)//2
    if cutting(mid): bot = mid+1
    else: top = mid-1
print(top)
  
