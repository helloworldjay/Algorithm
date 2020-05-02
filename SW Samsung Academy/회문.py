def palin(s):
    rev = s[::-1] # s를 거꾸로 출력
    if s[:len(s)//2] == rev[:len(s)//2]:
        return True
    return False

t = int(input()) # testcase 개수
result = [] # 결과 리스트
for _ in range(t):
    n , m = map(int,input().split()) # n x n 행렬의 길이, m = 회문의 길이
    nlist = []
    isCheck = False
    isCheck2 = False
    for i in range(n): # n 행을 입력받음
        nlist.append(input())
    # 회문이 가로로 존재
    for i in range(n):
        temp = nlist[i]    
        for j in range(n-m+1):
            if palin(temp[j:j+m]):
                result.append(temp[j:j+m])
                isCheck = True
                isCheck2 = True
                break    
        if isCheck :
            break
    if isCheck2 :
        continue
    # 회문이 세로로 존재
    for i in range(n):
        isCheck3 = False
        temp = []
        for j in range(n):
            temp.append(nlist[j][i])
        for j in range(n-m+1):
            if palin(temp[j:j+m]):
                result.append(''.join(temp[j:j+m]))
                isCheck3 = True
                break    
        if isCheck3 :
            break
for i in range(t):
    print("#{} {}".format(i+1, result[i]))    

