class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque


# 나의 풀이
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list == head_list[::-1]

# 책에 나온 풀이
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num_list = deque([])
        while head is not None: # head.val is not None은 안됨
            num_list.append(head.val)
            head = head.next
        while len(num_list) > 1:
            if num_list.popleft() == num_list.pop():
                continue
            return False
        return True