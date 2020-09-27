def solution(A):
    check = {}
    for i in range(len(A)):
        check[A[i]] = check.get(A[i], 0) + 1
    return len(check.keys())
    
def solution(A):
    return len(set(A))
