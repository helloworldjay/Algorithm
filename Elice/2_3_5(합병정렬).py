import math
def mergeSort(data) :
    '''
    n개의 숫자를 합병정렬을 이용하여 정렬한 결과를 list로 반환하는 함수를 작성하세요.
    '''
    # 기저 조건을 생성 : data의 요소가 1개 남을때 까지 나눈다
    if len(data) == 1:
        return data
    # 기저 조건이 아닐 때
    mid = len(data)//2
    # 병합하기 전 요소들을 정렬해야한다
    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])
    # 비교를 위해 관찰할 idx
    leftidx = 0
    rightidx = 0
    result = []
    # 병합하는 과정
    while leftidx < len(left) or rightidx < len(right):
        leftVal = left[leftidx] if leftidx < len(left) else math.inf
        rightVal = right[rightidx] if rightidx < len(right) else math.inf
        if leftVal > rightVal:
            result.append(rightVal)
            rightidx += 1
        else:
            result.append(left[leftidx])
            leftidx += 1
    

    return result