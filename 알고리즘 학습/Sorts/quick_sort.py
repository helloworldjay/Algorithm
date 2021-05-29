# def quick_sort(array: list) -> list:
#     if len(array) <= 1:
#         return array
#     pivot = array[len(array)//2]
#     left, same, right = [], [], []
#     for element in array:
#         if element < pivot:
#             left.append(element)
#         elif element > pivot:
#             right.append(element)
#         else:
#             same.append(element)
#     return quick_sort(left) + same + quick_sort(right)


def quick_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    left, mid, right = [], [], []
    pivot = array[len(array)//2]
    for element in array:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            mid.append(element)
    return quick_sort(left) + mid + quick_sort(right)
print(quick_sort([2,4,3,1,5]))