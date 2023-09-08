'''
206. REVERSE LINKED LIST
https://leetcode.com/problems/reverse-linked-list/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                nxt = curr.next
                curr.next = prev
                return reverse(nxt, curr)

        return reverse(head, None)
