# def solution(arr1, arr2):
#     import numpy as np
#     return np.dot(arr1,arr2).tolist()

def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr1[0])
    arr3 = []
    for i in range(a):
        sum = 0
        for j in range(b):
            sum += arr1[i][j]*arr2[j][i]
        arr3.extend(sum)
    return 


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))