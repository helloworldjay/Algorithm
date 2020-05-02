# 1946번
# 들어온 점수를 정렬하여 비교한다. 
t = int(input()) # testcase
result = [] # 결과 저장
for _ in range(t):
    n = int(input()) # 사람 수
    cnt = n # 총 사람수
    score = [] # 점수
    for _ in range(n):
        a, b = map(int, input().split()) # 점수 2종류
        score.append([a,b])
    score.sort(key = lambda x : -x[0])
    for i in range(n-1):
        for j in range(i+1,n):
            if score[i][1] > score[j][1] : # 첫 순위가 더 낮은 사람이 두번째 순위까지 
                cnt -= 1
                break
    result.append(cnt)
for i in range(t):
    print(result[i])