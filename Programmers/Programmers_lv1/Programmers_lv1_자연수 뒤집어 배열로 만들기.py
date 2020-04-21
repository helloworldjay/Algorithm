def solution(n):
    nlist = list(str(n))
    newnlist = []
    for i in range(len(nlist)):
        newnlist.append(int(nlist[len(nlist)-1-i]))
    return newnlist

print(solution(12345))