'''
199. BINARY TREE RIGHT SIDE VIEW
https://leetcode.com/problems/binary-tree-right-side-view/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        queue = [root]
        res = []

        while queue:
            lastVal = None

            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    lastVal = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            
            if lastVal is not None:
                res.append(lastVal)
        
        return res