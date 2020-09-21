from sys import stdin
input = stdin.readline
N = int(input())
cache = [0]*(N+1) # N을 만드는데 필요한 최소 제곱수의 개수 
for i in range(N+1):
    cache[i] = i # 1로만 표현하는 경우
    for j in range(1,i): # sqrt로 생각하지말고 역으로 제곱으로 접근하면 된다.
        if j*j > i: break
        if cache[i] > cache[i-j*j]+1: cache[i] = cache[i-j*j]+1
print(cache[N])