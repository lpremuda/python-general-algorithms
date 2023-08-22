'''
226. INVERT BINARY TREE
https://leetcode.com/problems/invert-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root None, do nothing and return function, meant for corner case where root is None
        if not root:
            return None
        
        # Traverse down left side of BST first, then right side
        # Note: Not taking output from these functions because the data structure is mutable
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Swap nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # Return is meant for the final return of the function
        return root