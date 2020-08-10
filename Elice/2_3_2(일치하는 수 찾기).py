# 정렬된 n개의 숫자 중 정수 m과 가장 가까운 값 찾기

# 재귀 없이 풀이
def findNum(n, m):
    # 시작 인덱스와 끝 인덱스
    start = 0
    end = len(n)-1
    while True:
        mid = (start+end)//2
        # 중간 값이 타겟과 같을 때 출력
        if n[mid] == m :
            return n[mid]
        # 종료 조건, 요소가 2개만 남았을 때 차이가 작은 것 출력
        elif end - start == 1:
            if abs(m-n[start]) > abs(n[end]-m):
                return n[end]
            else:
                return n[start]
        if n[mid] < m :
            start = mid
        else :
            end = mid

# 재귀로 풀이
def getNearestNum(n,m):
    if len(n) == 1:
        return (n[0],n[0])
    elif len(n) == 2:
        return (n[0],n[1])
    
    mid = len(n)//2

    if n[mid] >= m:
        # mid가 포함 될 수 있으므로 항상 mid가 범위에 포함 되어야 한다.
        return getNearestNum(n[:mid+1],m)
    else :
        return getNearestNum(n[mid:],m)
        
def getNumber(n,m):
    cknum1, cknum2 = getNearestNum(n,m)
    if abs(cknum2-m)>abs(m-cknum1):
        return cknum1
    else:
        return cknum2


n = list(map(int,input().split()))
m = int(input())

print(getNumber(n,m))


    
            
    