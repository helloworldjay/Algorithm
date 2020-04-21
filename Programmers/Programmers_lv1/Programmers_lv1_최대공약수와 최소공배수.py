def solution(n, m):
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
    return [gcd, lcm]

print(solution(2,5))