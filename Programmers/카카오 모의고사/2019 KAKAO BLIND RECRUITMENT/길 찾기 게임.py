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