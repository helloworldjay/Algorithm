def solution(A):
    # A를 순회하며 원의 양 끝점을 만든다.
    disc_edge = []
    for i, v in enumerate(A):
        disc_edge.append((i-v, -1)) # 왼쪽 끝
        disc_edge.append((i+v, 1)) # 오른쪽 끝
    disc_edge.sort() # disc_edge를 정렬하여 왼쪽 끝 포인트부터 확인을 시작한다.
    intersection = 0 # 겹치는 원의 개수
    interval = 0 # 열리기 시작하여 아직 닫히지 않은 원의 개수
    for i in range(len(disc_edge)):
        if disc_edge[i][1] == 1 : # 원의 오른쪽 끝
            interval -= 1 # 열려있는 원이 하나 줄어든다.
        if disc_edge[i][1] == -1 : # 원의 왼쪽 끝(새로 열릴 때)
            intersection += interval # 기존에 열려있던 원들과 겹치게 되어 총 쌍의 수에 포함이 된다.
            interval += 1 
    return intersection if intersection <= 10000000 else -1

print(solution([1, 5, 2, 1, 4, 0]))
