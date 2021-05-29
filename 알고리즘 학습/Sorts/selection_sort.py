def selection_sort(array: list) -> list:
    for i in range(len(array)-1):
        min_index = array.index(min(array[i:]))
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
    return array

print(selection_sort([2,5,3,4,1]))

# O(N^2) 그래도 bubble_sort보다 실제 속도는 빠르다
# 최소 인덱스를 비교하는 과정에서 메모리가 더 소모될 수 있지만 교환 횟수가 적기 때문에
# 장점은 구현이 쉽다.
