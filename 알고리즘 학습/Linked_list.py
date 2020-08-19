# 데이터와 포인터, 두가지를 저장할 공간을 만들기 위해 클래스를 이용하면 더 수월하다
class Node :
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None # 주소를 저장하는 곳
    

    def __init__(self, data, next = None):
        self.data = data # 데이터 저장
        self.next = next # 포인터(주소) 저장

    def add(self, data):
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)

    
node1 = Node(1)
node2 = Node(2)
# node1의 주소 부분을 node2로 선언해준다. 
node1.next = node2
# 가장 앞의 노드는 반드시 알아야 하므로 head로 그 위치를 표시한다.
head = node1

for idx in range(1,10):
    node1.add(idx)
node = head
while node.next:
    print(node.data)

