'''
104. MAXIMUM DEPTH OF BINARY TREE
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        res = 0

        while queue:
            node_present_on_this_level = False

            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    node_present_on_this_level = True
                    queue.append(node.left)
                    queue.append(node.right)
                
            if node_present_on_this_level:
                res += 1
        
        return res
