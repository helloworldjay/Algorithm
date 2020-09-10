import sys
sys.setrecursionlimit(10**6)

class Tree:
    
    def __init__(self, dataList):
        # y번째 요소를 기준으로 정렬한다.
        self.data= max(dataList, key=lambda x:x[1])
        # x값을 기준으로 루트노드의 x보다 작은 값은 왼쪽 리스트에 넣는다.
        leftList = list(filter(lambda x:x[0]< self.data[0], dataList))
        rightList = list(filter(lambda x: x[0]>self.data[0],dataList))

        if leftList != []:
            leftList = Tree(leftList)
        else :
            leftList = None

        if rightList != []:
            rightList = Tree(rightList)
        else :
            rightList = None

def search(node, preList, postList):
    # 루트노드부터 방문한다.
    preList.append(node.data)
    # 만약 왼쪽이 비어있지 않으면 다시 왼쪽 노드를 순회
    if node.leftList is not None:
        search(node.leftList,preList,postList)
    if node.rightList is not None:
        search(node.rightList, preList, postList)
    postList.append(node.data)


def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    preList = []
    postList = []
    search(root, preList, postList)

    answer.append(list(map(lambda x: nodeinfo.index(x)+1, preList)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1, postList)))
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))


# 용철이 코드
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,number,x):
        self.number = number
        self.x = x
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None
    
    # number = index+1, x는 이 number를 가지고있는 노드의 x값
    # 바깥에서 호출되는 insert
    def insert(self,number,x):
        self.root = self._insert(self.root,number,x)
    
    # 내부적으로 실제로 돌아가는 insert
    def _insert(self,node,number,x):
        if node == None:
            new_node = Node(number,x)
            return new_node
        else:
            if x > node.x:
                node.right = self._insert(node.right,number,x)
            else:
                node.left = self._insert(node.left,number,x)
        return node
    
    def preorder(self):
        lis = []
        def _preorder(node):
            lis.append(node.number)
            if node.left != None: _preorder(node.left)
            if node.right != None: _preorder(node.right) 
        _preorder(self.root)
        return lis

    def postorder(self):
        lis = []
        def _postorder(node):
            if node.left != None: _postorder(node.left)
            if node.right != None: _postorder(node.right)
            lis.append(node.number) 
        _postorder(self.root)
        return lis

def solution(nodeinfo):
    idx = [i for i in range(1,len(nodeinfo)+1)]
    nodeinfo = list(zip(idx,nodeinfo))
    nodeinfo.sort(key = lambda x : x[1][1], reverse = True)
    
    tree = Tree()
    for i,l in nodeinfo:
        tree.insert(i,l[0])
    pr = tree.preorder()
    po = tree.postorder()
    return [pr,po]
