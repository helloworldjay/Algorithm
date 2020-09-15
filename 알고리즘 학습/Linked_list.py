class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    def delete(self,data):
        if self.head == '':
            print("data가 없습니다.")
            return

        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else: # node의 head가 아닌 값을 삭제할 경우
            node = self.head
            # node의 다음값이 존재하는 동안
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = temp.next
                    del temp
                else:
                    node = node.next
            


linkedlist1 = NodeMgmt(0)
# linkedlist1.add(1)
# linkedlist1.add(2)
# linkedlist1.add(3)


for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()