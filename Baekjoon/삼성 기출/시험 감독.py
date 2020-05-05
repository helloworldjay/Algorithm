import math
N = int(input()) # 시험장의 개수
A = list(map(int, input().split()))
b, c = map(int, input().split()) # 주 감독관, 부 감독관이 커버 가능한 응시생 수
cnt = 0 # 감독관 수
for i in range(N):
    temp = A[i]
    # 주감독관 배치
    temp -= b
    cnt += 1
    if temp <= 0:
        continue
    # 부감독관 배치
    cnt += math.ceil(temp/c)
print(cnt)
