# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


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