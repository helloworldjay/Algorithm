n, m, k = map(int, input().split()) # n 여학생, m 남학생, k 인턴
# k 값을 어디서 뺄지 하나씩 경우를 세며 따져본다.  
mx = 0 # 최대 개수
for i in range(k+1):
    tempn = n - i
    tempm = m - k + i
    cnt = tempm if tempn >= tempm*2 else tempn//2
    if cnt > mx:
        mx = cnt
print(mx)
