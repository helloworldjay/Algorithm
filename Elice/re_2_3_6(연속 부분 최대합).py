def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    '''
    n = len(data)
    # 기저조건
    if n == 1 :
        return data[0]
    
    mid = n//2

    left = getSubsum(data[:mid])
    right = getSubsum(data[mid:])

    Sum = 0
    # 왼쪽, 오른쪽 부분에서 각각 가장 큰 부분합을 담을 변수
    leftSum = 0
    rightSum = 0
    
    for i in range(mid-1,-1,-1):
        Sum += data[i]
        leftSum = max(Sum, leftSum)
    Sum = 0
    for i in range(mid,n):
        Sum += data[i]
        rightSum = max(Sum, rightSum)
    # ?
    return max([left,right,leftSum+rightSum])