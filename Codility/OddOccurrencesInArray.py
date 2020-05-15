def solution(A):
    ck = {}
    for i in range(len(A)):
        if A[i] not in ck :
            ck[A[i]] = 1
        elif ck[A[i]] :
            ck[A[i]] = 0
        elif not ck[A[i]] :
            ck[A[i]] = 1
    cklist = sorted(list(ck.items()), key = lambda x : -x[1])
    return cklist[0][0]