# 종만북(알고리즘 문제해결전략)
# 7장

# what I found : 파이썬에선 파일명 등에 숫자 앞에 0이 붙는 08, 02 등의 표현을 사용하면 에러가 발생한다.

import chap6

# recursiveSum 함수의 경우 O(N)으로 동작한다.
# 이를 분할정복으로 돌려 빠른 연산을 수행할 수 있다.
# 아래 fastSum의 경우 O(logN)의 시간복잡도를 가진다.

def fastSum(n):
    # 기저 사례
    if n == 1 : return 1
    # n이 홀수 일 때
    # 홀수일 때 n//2, n//2+1 가지로 원소를 나누어 처리하는 것보다 하나만 빼고 짝수로 만들어 처리하는 것이 연산 속도가 더 빠르다.
    if n%2 == 1:
        return fastSum(n-1) + 1
    # n이 짝수 일 때 1+2+..+n = 1+2+..+(n//2)+ ((n//2)+1)+..((n//2)+(n//2)) 이므로
    return 2*fastSum(n//2) + (n//2)*(n//2)

