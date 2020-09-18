mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
import heapq

def dijkstra(graph, start):
    # A에서 특정 노드로 가는데 걸리는 최소거리를 inf로 초기화
    distances = {node:float('inf') for node in graph} # float('inf')는 math.inf와 같다.
    # start에서 start까지는 거리가 0이다
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start]) # 초기값을 start와 start에서 start까지 거리를 넣어준다.

    while queue:
        # 시작점에서 현재 노드까지의 거리와 그 현재 노드
        current_distance, current_node = heapq.heappop(queue)
        # 이미 시작점에서 현재노드까지의 거리가 저장되어있는 시작점에서 현재노드까지의 거리보다 길면 
        # 더 계산할 이유가 없으므로 for문을 안돌고 pruning한다.
        if distances[current_node] < current_distance:
            continue
        # adjacent는 인접한 노드값, weight는 current_node에서 거기까지의 거리
        for adjacent, weight in graph[current_node].items():
            # 거리는 시작점에서 현재노드까지의 거리에다가 그 노드에서 연결된 노드들 까지의 거리의 합
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances

print(dijkstra(mygraph,'A'))

    
