# 1번 15분
def solution(n, delivery):
    store = [0 for i in range(n+1)] # 재고 상태 확인 -1은 없다, 0은 모른다, 1은 있다
    for i in range(len(delivery)):
        if delivery[i][2] == 1: # 배송이 가능한 경우 확실히 있다로 표시
            store[delivery[i][0]] = 1
            store[delivery[i][1]] = 1
    for i in range(len(delivery)):
        if delivery[i][2] == 0: # 배송 불가능한 경우
            # 둘중에 하나가 확실히 재고가 있는 경우 나머지는 없음
            if store[delivery[i][0]] == 1 : 
                store[delivery[i][1]] = -1
            elif store[delivery[i][1]] == 1 :
                store[delivery[i][0]] = -1
    result = ''
    for i in range(1, n+1):
        if store[i] == -1 : result += 'X'
        elif store[i] == 0 : result += '?'
        elif store[i] == 1 : result += 'O'
    return result

print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))