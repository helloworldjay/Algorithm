def crain(board, n) :
    for i in range(len(board)):
        if board[i][n-1] != 0 :
            result = board[i][n-1]
            board[i][n-1] = 0
            return result # 크레인으로 들어올린 물품
    return -1
def solution(board, moves):
    cnt = 0
    stk = [0]
    for i in moves:
        cp = crain(board,i) # 조건문 안에 crain 함수를 넣어두니 작동을 안한 것으로 인식한다. board를 바꾸지 않았다.
        if stk[-1] == cp:
            cnt += 2
            stk.pop()
        elif cp != -1:
            stk.append(cp) 
        
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))