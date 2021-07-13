# 연결 해쉬 만들기 


def findcon(start):
    # 시작을 기준으로 연결된 네트워크를 탐색하느 ㄴ함수



def solution(n, computers):
    con = [[] for i in range(n)] # 꼭 딕셔너리가 될 필요가 없다.
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1 :
                if i != j :
                    con[i].append(j)
    return con

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))