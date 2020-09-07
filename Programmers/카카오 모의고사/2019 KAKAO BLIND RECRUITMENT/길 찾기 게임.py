# 전위 순회를 구현 (순회할 노드, 시작노드)
# 전위 순회는 DFS이므로 스택구조이기 때문에 오른쪽, 왼쪽 노드 순으로 입력이 되어있어야한다.
# 왼쪽부터 관찰하기 위해
def preorder(node, start_node):
    visiting = [start_node]
    result = []
    while visiting:
        # 체크할 노드를 꺼낸다.
        check_node = visiting.pop()
        visiting.extend(node[check_node])
        result.append(check_node)
    return result

def postorder(node, start_node,len_node):
    visited = [0] * (len_node+1)
    visiting = [start_node]
    result = []
    while visiting:
        # 가장 바깥 값을 관찰
        check_node = visiting[-1]
        # 만약 연결이 되어 있다면
        if node[check_node] and visited[check_node] == 0:
            # 연결된 노드수만큼 순회
            for i in range(len(node[check_node])):
                # 관찰 노드로 추가
                visiting.append(node[check_node][i])
            # 방문을 표시
            visited[check_node] = 1
        else:
            check_node = visiting.pop()
            result.append(check_node)
    return result
dic = {1:[3,2],2:[5,4],3:[7,6],4:[],5:[],6:[],7:[]}

def solution(nodeinfo):
    # node를 번호로 입력하기 위한 리스트
    node = []
    # 노드를 담을 dict
    node_dict = {}
    # nodeinfo에 번호를 붙여주어야 한다.
    for i, ele in enumerate(nodeinfo):
        node.append((i+1, ele)) 
    # nodeinfo를 인덱스 1값, 그 다음 0 값을 기준으로 역순 정렬한다.
    node.sort(key = lambda x: (x[1][1],x[1][0]), reverse = True)
    # 가장 높은 위치를 찾는다.
    top = node[0][1][1]
    idx = 0
    parents = [node[0]]
    while True:
        temp = []
        if node[idx][1][1] == top:
            temp.append(node[idx])
        
    return node

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))