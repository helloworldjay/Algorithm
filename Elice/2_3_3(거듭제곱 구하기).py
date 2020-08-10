# m^n 구하기
LIMIT_NUMBER = 1000000007

def getPower(m, n):
    # return getPower(m,n-1) * m 은 O(N) 의 선형 시간이 걸려 속도가 느리다.
    # n이 짝수일 때와 홀수일 때로 나눈다.
    # 기저 조건(n == 1이면 반환을 시작한다)을 만들어야한다.
    # 기저 조건을 n == 1이 아니라 n == 0 이면 1로 하였다.
    # 기저 조건이 n == 1이면 recursive depth 오류가 발생한다.
    if n == 0:
        return 1
    
    if n % 2 == 0:
        half = getPower(m, n//2)
        return  (half * half) % LIMIT_NUMBER
    else:
        half = getPower(m, (n-1)//2)
        return (half * half * m) % LIMIT_NUMBER