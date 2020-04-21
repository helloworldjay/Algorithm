def findLcm(n, m):
    orin,orim = n, m
    #gcd
    if n == m :
        return [n, n]
    elif n > m : #대소 비교
        n,m = m,n 
    while True :
        remainder = m%n
        if remainder == 0 :
            gcd = n
            break
        else : 
            m , n = n , remainder
    #lcm
    lcm = (orin*orim)//gcd
    return lcm

def solution(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        lcm = findLcm(lcm,arr[i])
    return lcm

print(solution([1,2,3]))