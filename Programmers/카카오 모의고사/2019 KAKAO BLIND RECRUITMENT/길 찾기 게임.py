import sys
sys.setrecursionlimit(10**6)

preorder = []
postorder = []

class Tree:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left=self.right = None

# 전위순회
def preorder_func(node):
    # 먼저 루트노드의 인덱스를 넣는다.(node를 삽입할 때 이미 idx+1 처리를 해줌)
    preorder.append(node.index)
    # 왼쪽 노드가 존재하면 다시 방문하여 거기서 다시 전위순회
    if node.left:
        preorder_func(node.left)
    # 오른쪽 노드가 존재하면 방문하여 다시 전위순회
    if node.right:
        preorder_func(node.right)

# 후위순회
def postorder_func(node):
    # 왼쪽을 먼저 방문
    if node.left:
        postorder_func(node.left)
    # 오른쪽 방문
    if node.right:
        postorder_func(node.right)
    # rootnode를 넣어준다.
    postorder.append(node.index)


def solution(nodeinfo):
    answer = []
    # 하나의 리스트로 요소를 만들어 [x,y,index]로 만들어준다. 
    nodeinfo_index = [info + [idx+1] for idx, info in enumerate(nodeinfo)]
    nodeinfo_index.sort(key = lambda x : (x[1], x[0]), reverse= True)
    root_node = None
    # y를 기준으로 역순정렬이므로 부모 노드부터 시작한다.
    for node in nodeinfo_index:
        # rootnode가 비어있으면
        if not root_node:
            # Tree라는 객체를 x,y,index로 생성해준다. 이 경우 left와 right은 None인 상태가 된다. 
            root_node = Tree(node[0],node[1],node[2])
        # rootnode가 차 있으므로 
        else:
            # node의 x값
            x = node[0]
            cur_node = root_node
            while True:
                # 이번 노드의 x좌표가 부모노드의 x좌표보다 작다면
                if x < cur_node.x:
                    # 만약 left가 차 있다면
                    if cur_node.left:
                        # 다시 현재노드에 왼쪽노드를 넣어주고 돌린다.
                        cur_node = cur_node.left
                        # x값에 변화를 안준 상태로 다시 한칸 더 들어간다.
                        continue
                    # left가 비어있으면
                    else:
                        # 현재 노드의 왼쪽에 지금 노드들을 넣어준다.
                        cur_node.left = Tree(node[0],node[1],node[2])
                        # 현재 관찰 노드가 안착되었으므로 반복을 종료한다.
                        break
                elif x > cur_node.x:
                    if cur_node.right:
                        cur_node = cur_node.right
                        continue
                    else:
                        cur_node.right = Tree(node[0],node[1],node[2])
                        break
                break
    # rootnode로 탐색을 시작한다.
    preorder_func(root_node)
    postorder_func(root_node)
    answer.append(preorder)
    answer.append(postorder)
    return answer
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

# 용철이 코드
# import sys
# sys.setrecursionlimit(10**6)

# class Node:
#     def __init__(self,number,x):
#         self.number = number
#         self.x = x
#         self.right = None
#         self.left = None

# class Tree:
#     def __init__(self):
#         self.root = None
    
#     # number = index+1, x는 이 number를 가지고있는 노드의 x값
#     # 바깥에서 호출되는 insert
#     def insert(self,number,x):
#         self.root = self._insert(self.root,number,x)
    
#     # 내부적으로 실제로 돌아가는 insert
#     def _insert(self,node,number,x):
#         if node == None:
#             new_node = Node(number,x)
#             return new_node
#         else:
#             if x > node.x:
#                 node.right = self._insert(node.right,number,x)
#             else:
#                 node.left = self._insert(node.left,number,x)
#         return node
    
#     def preorder(self):
#         lis = []
#         def _preorder(node):
#             lis.append(node.number)
#             if node.left != None: _preorder(node.left)
#             if node.right != None: _preorder(node.right) 
#         _preorder(self.root)
#         return lis

#     def postorder(self):
#         lis = []
#         def _postorder(node):
#             if node.left != None: _postorder(node.left)
#             if node.right != None: _postorder(node.right)
#             lis.append(node.number) 
#         _postorder(self.root)
#         return lis

# def solution(nodeinfo):
#     idx = [i for i in range(1,len(nodeinfo)+1)]
#     nodeinfo = list(zip(idx,nodeinfo))
#     nodeinfo.sort(key = lambda x : x[1][1], reverse = True)
    
#     tree = Tree()
#     for i,l in nodeinfo:
#         tree.insert(i,l[0])
#     pr = tree.preorder()
#     po = tree.postorder()
#     return [pr,po]
