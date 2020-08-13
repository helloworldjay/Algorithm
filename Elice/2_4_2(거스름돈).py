def coinChange(n) :
    '''
    n원을 돌려주기 위해 필요한 동전 개수의 최솟값을 반환하는 함수를 작성하세요.
    '''
    cointype = [100,50,10,5,1]
    coinNum = 0
    for i in range(5):
        if n == 0:
            break
        coinNum += n // cointype[i]
        n %= cointype[i]

    return coinNum
