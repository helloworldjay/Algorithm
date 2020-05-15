def solution(A):
    right = sum(A[1:])
    left = A[0]
    minv = abs(right - left)
    for i in range(1, len(A)-1):
        right -= A[i]
        left += A[i]
        if minv > abs(right-left):
            minv = abs(right-left)
    return minv