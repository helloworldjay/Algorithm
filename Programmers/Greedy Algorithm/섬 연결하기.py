# 0부터 시작해서 모든 점을 연결할 수 있는지 확인
# def search(start, n, connection):
#     from collections import deque
#     visited = [0 for _ in range(n)]
#     visiting = deque([start])
#     while visiting:
#         to_visit = visiting.popleft()
#         if not visited[to_visit]:
#             visited[to_visit] = 1
#             visiting.extend(connection[to_visit])
#     return sum(visited) == n
#
# def solution(n, costs):
#     costs.sort(key=lambda x: x[2])
#     connection = {i: [] for i in range(n)}
#     total_price = 0
#     for cost in costs:
#         start, end, price = cost
#         connection[start].append(end)
#         connection[end].append(start)
#         total_price += price
#         if search(0, n, connection):
#             return total_price
#     return total_price

def solution(n, costs):
    total_price = 0
    costs.sort(key=lambda x: x[2])
    con = set([0])
    while len(con) != n:
        for cost in costs:
            start, end, price = cost
            if start in con or end in con:
                if start in con and end in con:
                    continue
                else:
                    con.add(start)
                    con.add(end)
                    total_price += price
                    break
    return total_price

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))