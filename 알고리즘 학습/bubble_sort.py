# bubble sort
# O(n^2)

def bubble_sort(lst):
    # 범위의 끝 위치 설정
    for i in range(len(lst)-1,0,-1):
        # 마지막 원소를 결정하기 위한 연산 요소
        # 두 항목을 비교해서 큰 쪽을 오른쪽으로
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print(bubble_sort([1,4,6,2,6,4]))