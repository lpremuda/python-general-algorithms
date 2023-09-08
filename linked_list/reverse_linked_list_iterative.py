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
        # Initialize two pointers: prev and curr
        prev = None
        curr = head

        # While curr is a valid node
        while curr:
            nxt = curr.next
            curr.next = prev
            # Update prev and curr pointers to next nodes
            prev = curr
            curr = nxt
        
        # prev should always be pointing to the last valid node anc curr will be pointing to None
        return prev
