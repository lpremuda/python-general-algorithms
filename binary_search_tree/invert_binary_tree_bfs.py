'''
226. INVERT BINARY TREE
https://leetcode.com/problems/invert-binary-tree/
'''

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Corner case if root is None
        if not root:
            return None
        
        # Initialize deque with root node
        q = deque()
        q.append(root)
        
        while q:
            # Pop off next node in queue
            curr_node = q.popleft()

            # Swap nodes
            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp

            # Add child nodes to queue if they are not None
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)

        return root