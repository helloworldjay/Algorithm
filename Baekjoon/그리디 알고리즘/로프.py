n = int(input()) # 밧줄의 개수
ropes = [] 
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()
mx = 0 # 최대 무게
for i in range(1, n+1): # i는 사용하는 밧줄의 개수
    if mx < ropes[-i]*i:
        mx = ropes[-i]*i
print(mx)