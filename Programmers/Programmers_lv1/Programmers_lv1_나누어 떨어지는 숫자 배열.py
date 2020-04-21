def solution(arr, divisor):
    import bisect
    arr2 =[]
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            bisect.insort(arr2, arr[i])
    if len(arr2) != 0 :
        return arr2
    else :
        return [-1]
print(solution([3,2,6],10))
