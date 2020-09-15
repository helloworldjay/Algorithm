class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class NodeMgnt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.currentnode = self.head
        while True:
            if value < self.currentnode.value: # insert할 value가 현재 노드의 value보다 작다면 왼쪽을 본다.
                if self.currentnode.left != None: # 왼쪽 노드가 차있다면
                    self.currentnode = self.currentnode.left # 왼쪽노드를 현재노드로 바꿔서 다시 실행
                else: # 왼쪽 노드가 비어있다면 그냥 노드 자체를 넣어준다.
                    self.currentnode.left = Node(value)
                    break
            else : # value가 현재 노드의 value보다 크거나 같으면 오른쪽으로 간다.
                if self.currentnode.right != None:
                    self.currentnode = self.currentnode.right
                else: # 오른쪽이 비어있다면
                    self.currentnode.right = Node(value)
                    break

    def search(self, value): # 해당 트리에 value값이 존재하는지 확인
        self.currentnode = self.head
        while self.currentnode:
            if value == self.currentnode.value: # value가 tree상에 존재하므로 True 출력
                return True
            elif value < self.currentnode.value: # value가 현재 노드의 value보다 작다면
                self.currentnode = self.currentnode.left # 왼쪽으로 내려가서 관찰 계속
            else :
                self.currentnode = self.currentnode.right # value가 currentnode의 value보다 크면 오른쪽으로 내려간다.
        return False
    

head = Node(1)
check = NodeMgnt(head)
for i in range(2,10):
    check.insert(i)
print(check.search(9))


    