def merge(left, right):
    left_idx, right_idx = 0, 0
    result = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result += left[left_idx:] if left_idx < len(left) else right[right_idx:]
    return result

def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    left, right = merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:])
    return merge(left, right)

print(merge_sort([2,5,3,4,1]))

# 장점 고정된 준수한 속도 O(NlogN) why?
# 단점 메모리의 추가적인 소비