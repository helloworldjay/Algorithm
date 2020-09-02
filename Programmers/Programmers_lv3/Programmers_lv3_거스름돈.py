# n 원, money는 거스름돈의 종류를 담은 list
def solution(n, money):
    # cache[x][y] 는 동전 1~x로 y원을 만들기
    cache = [[0 for i in range(n+1)] for j in range(len(money))]
    # 0,0을 초기화
    cache[0][0] = 1
    # 최소의 크기 동전으로 금액을 만들 수 없는 경우가 존재
    # money[0]의 배수만 거스름돈으로 만들수 있으므로 갱신
    for i in range(money[0],n+1,money[0]):
        cache[0][i] = 1
    # money[1]부터 추가로 사용하며 cache 채우기
    for i in range(1, len(money)):
        # 0원부터 n원까지 만들어가기
        for j in range(n+1):
            # money[i]를 이용해 j원을 만들 방법이 없다.
            if j < money[i]:
                cache[i][j] = cache[i-1][j]
            # 방법이 존재하면
            else:
                # 동전 money[i]를 사용하지 않은 방법의 가지수 + 동전 money[i]를 한개 사용한 가지수
                cache[i][j] = (cache[i-1][j] + cache[i][j-money[i]])%1000000007
    return cache[len(money)-1][n]

print(solution(5, [1,2,5]))
