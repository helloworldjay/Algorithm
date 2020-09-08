import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

preorderList = []
postorderList = []

def preorder(node, nodeinfo):
    preorderList.append(nodeinfo.index(node.data)+1)



print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))