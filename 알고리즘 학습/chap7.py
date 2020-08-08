# 종만북(알고리즘 문제해결전략)
# 7장

# what I found : 파이썬에선 파일명 등에 숫자 앞에 0이 붙는 08, 02 등의 표현을 사용하면 에러가 발생한다.

# recursiveSum 함수의 경우 O(N)으로 동작한다.
# 이를 분할정복으로 돌려 빠른 연산을 수행할 수 있다.
# 아래 fastSum의 경우 O(logN)의 시간복잡도를 가진다.

def fastSum(n):
    # 기저 사례
    if n == 1 : return 1
    # n이 홀수 일 때
    # 홀수일 때 n//2, n//2+1 가지로 원소를 나누어 처리하는 것보다 하나만 빼고 짝수로 만들어 처리하는 것이 연산 속도가 더 빠르다.
    if n%2 == 1:
        return fastSum(n-1) + 1
    # n이 짝수 일 때 1+2+..+n = 1+2+..+(n//2)+ ((n//2)+1)+..((n//2)+(n//2)) 이므로
    return 2*fastSum(n//2) + (n//2)*(n//2)


# 병합 정렬(Merge Sort)
# 2로 나누고 1개의 요소가 남을 때 까지 재귀적으로 conquer
# 그 후 요소를 2개씩 병합해나간다.
def mergeSort(unsorted_list):
    # 기저조건 : 요소가 1개
    if len(unsorted_list) <= 1:
        # 요소가 아니라 리스트를 반환
        return unsorted_list
    # 가운데를 기준으로 나누기 위해 가운데 항목 찾기
    mid = len(unsorted_list)//2
    # 중간값을 기준으로 왼쪽 요소 
    left = unsorted_list[:mid]
    # 중간값을 기준으로 오른쪽 요소
    right = unsorted_list[mid:]
    # 재귀를 이용해 왼쪽값과 오른쪽값을 다시 나눈다.
    splited_left = mergeSort(left)
    splited_right = mergeSort(right)
    # 분리된 두 부분을 병합한 결과를 반환
    return merge(splited_left, splited_right)
# 병합하는 함수
def merge(left, right):
    # 시작점
    i,j = 0, 0
    sorted_list = []
    
    while i < len(left) and j < len(right):
        # 양 리스트를 앞부터 비교해가며 더 작은 것을 먼저 넣는다.
        if left[i] < right[j]:
            sorted_list.append(left[i])
            # i번째 요소를 넣었으므로 다음 것으로 갱신
            i += 1
        else :
            sorted_list.append(right[j])
            # j번째 요소를 넣었으므로 다음 것으로 갱신
            j += 1
    
    # 남은 요소가 존재할 경우 넣어준다.
    # while i < len(left):
    #     sorted_list.append(left[i])
    #     i += 1

    # while j < len(right):
    #     sorted_list.append(right[j])
    #     j += 1
    
    # 나의 풀이 
    if len(left) != i:
        sorted_list.extend(left[i:])
        i = len(left)
    else :
        sorted_list.extend(right[j:])
        j = len(right)
    return sorted_list

# 퀵소트(Quick Sort)
# pivot을 기준으로 pivot보다 작은 값은 왼쪽에, 큰 값은 오른쪽에 저장한다.
# 리스트 arr을 퀵소트 하는 함수
def quick_sort(arr):
    # 재귀 함수이며 정렬 범위를 시작 인덱스와 끝 인덱스로 받는다.(both inclusive)
    def sort(low, high):
        # 종료 조건(인덱스 역전)
        if high <= low :
            return 
        # 정렬 기준점을 mid에 넣는다
        mid = partition(low, high)
        # 정렬 기준점을 중심으로 왼쪽, 오른쪽을 각각 정렬한다.
        sort(low, mid-1)
        sort(mid,high)
    # 정렬 범위를 인자로 받으며 좌, 우측의 값들을 정렬하고 분할기준점의 인덱스를 리턴한다.
    def partition(low, high):
        # 중간값을 피봇으로
        pivot = arr[(low+high)//2]
        while low <= high:
            # 피봇값보다 피봇 왼쪽 값이 더 작다면 아무 작업을 안해도 되므로 변경이 필요할 때까지 다음 것으로 넘기기
            while arr[low] < pivot:
                low += 1
            # 피봇값보다 피봇 오른쪽 값이 더 크다면 아무 작업을 안해도 되므로 변경이 필요할 때까지 이전 것으로 당기기
            while arr[high] > pivot:
                high -= 1
            # 피봇 기준으로 변경이 필요
            if low <= high:
                # 두 값을 바꿔준다.
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high -1 
        return low

    return sort(0, len(arr)-1)