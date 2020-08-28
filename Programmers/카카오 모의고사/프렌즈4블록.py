# 90도 회전
def rotate(lst):
    N = len(lst)
    ret = [[0]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = lst[r][c]
    
    return ret


def solution(m, n, board):
    board = rotate(board)
    # 전체 순회하며 범위 내에서 기준값을 잡고, 그 주변에 3쌍씩을 확인한다. 
    # 3개가 모두 같은 모양이면 위치를 저장한다.
    # 전체 순회로 모두 저장한 뒤 해당값을 한번에 제거해준다.
    # 제거하며 뒷부분의 요소들을 앞으로 당겨준다.
    # 저장된 위치의 빈 칸에 구별 가능한 다른 요소를 채워준다.(예를 들어 0) 
    # 저장된 위치를 초기화 해준다.
    # 위치가 0이 아니며 범위를 벗어나는 구간에서 해당 과정을 반복한다.
    # 저장된 위치에 True가 없으면 반복을 종료하고 남은 요소들의 개수를 센다.
    # 전체 - (0의 개수)


    return 
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))