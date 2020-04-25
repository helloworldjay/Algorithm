# 연결 해쉬 만들기 


def solution(n, computers):
    con = {} # connection dictionary
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1 :
                
    return con

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))