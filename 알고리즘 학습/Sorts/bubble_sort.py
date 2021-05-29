def bubble_sort(array: list) -> list:
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# 각 시점에 가장 큰 값이 가장 뒤로 보내진다.

# 장점: 코드가 직관적, 구현이 쉬움
# 단점: 속도가 매우 느리다. 최악 최선 모두 O(N^2)

print(bubble_sort([2,5,3,4,1]))