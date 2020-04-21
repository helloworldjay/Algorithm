def solution(arr1, arr2):
    arr3 = [[0] * len(arr1[0]) for i in range(len(arr1))]
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            arr3[i][j] = (arr1[i][j] + arr2[i][j])
    return arr3

print(solution([[1],[2]],[[3],[4]]))
