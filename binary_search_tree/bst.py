# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def convertToSortedList(root) -> list[int]:

        def traverse(node, sortedList):
            if not node:
                return
            traverse(node.left, sortedList)
            sortedList.append(node.val)
            traverse(node.right, sortedList)

        sortedList = [] 
        traverse(root, sortedList)
        return sortedList



bst = TreeNode(3)
bst.left = TreeNode(1)
bst.right = TreeNode(5)
bst.left.left = TreeNode(0)
bst.left.right = TreeNode(2)
bst.right.left = TreeNode(4)
bst.right.right = TreeNode(6)

'''
[0,1,2]


'''

print(TreeNode.convertToSortedList(bst))