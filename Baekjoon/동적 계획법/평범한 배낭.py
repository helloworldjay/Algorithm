n, k = map(int, input().split()) # 물품의 수, 버틸 수 있는 무게 입력
cache = [[0]*(k+1) for _ in range(n+1)] # cache 가 for문 안에 들어가면 안된다.
# 리스트 컴프리핸션 숙지
for i in range(1, n+1):
    w, v = map(int, input().split()) # weight, value
    for j in range(1, k+1):
        if w > j:
            cache[i][j] = cache[i-1][j]
        else :   
            cache[i][j] = max(cache[i-1][j], cache[i-1][j-w] + v)

print(cache[n][k])