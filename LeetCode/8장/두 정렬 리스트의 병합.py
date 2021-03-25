# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val): # l1이 비어있거나 l1이 있으면서 l2도 있고 l1이 l2보다 크면 작은 수를 l1으로 넣어준다. l2가 없으면 뒤에 부등호가 오류가 발생하므로 l2가 있는지 확인한다.
            l1, l2 = l2, l1
        if l1: # l1이 있을 경우의 의미는 위의 조건 때문에 l1과 l2중 어느하나라도 있으면이라는 뜻이 된다.
            l1.next = self.mergeTwoLists(l1.next, l2) # l1의 뒤에 다음 것을 이어붙이는 부분 문제가 된다.
        return l1 # 현재 노드를 반환하여 이 함수의 최종 반환 값은 첫 노드가 되고, 이후에는 위의 함수에서 다음 노드가 붙는 구조가 되므로 l1을 반환한다.
