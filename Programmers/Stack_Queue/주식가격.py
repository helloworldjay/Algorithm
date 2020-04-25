# 첫번째 요소부터 자기보다 작은 수가 나올 때까지 검색하여 idx 차이를 저장

def solution(prices):
    from collections import deque
    prices = deque(prices)
    queue = []
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i] > prices[j] :
                queue.append(j-i)
            elif j == len(prices)-1:
                queue.append(j-i)
    return queue