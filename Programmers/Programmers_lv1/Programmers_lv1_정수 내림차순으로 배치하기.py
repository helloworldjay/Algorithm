def solution(n):
    nlist = list(str(n))
    nlist.sort(reverse = True)
    
    return int(''.join(nlist))

print(solution(118372))


