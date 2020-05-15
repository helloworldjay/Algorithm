def solution(N, A):
    ck = [0]*N
    mx = 0
    tmp = 0
    for i in range(len(A)):
        if A[i] < N+1:
            ck[A[i]-1] += 1
            if ck[A[i]-1] > mx:
                mx = ck[A[i]-1]
        
    return ck