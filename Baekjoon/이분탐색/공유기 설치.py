from sys import stdin
input = stdin.readline
N, C = map(int, input().split())
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()
end = home[-1]-home[0] # 공유기 간 최대 거리
start = 1 # 공유기 간 최소 거리
def setting(distance,C):
    set_point = 0
    C -= 1
    for i in range(1, N):
        if home[i] >= home[set_point]+distance:
            set_point = i
            C -= 1
        if C == 0 : return True
    return False
while start <= end:
    mid = (start+end)//2
    if setting(mid, C): start = mid+1
    else : end = mid-1
print(end)
    