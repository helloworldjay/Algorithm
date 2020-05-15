def solution(X, A):
    ck = [i for i in range(X+1)]
    cnt = 0
    for k in range(len(A)):
        if A[k] < X+1:
            if ck[A[k]] != 0 :
                ck[A[k]] = 0
                cnt += 1
            if cnt == X:
                return k
    return -1
    
    
