def solution(n, s, a, b, fares):
    root = {}
    for i in range(len(fares)):
        node1, node2 = fares[i][0], fares[i][1]
        # 연결 노드와 그 가격을 저장
        root[node1] = root.get(node1, []) + [(node2, fares[i][2])]
        root[node2] = root.get(node2, []) + [(node1, fares[i][2])]
    
    return root

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))