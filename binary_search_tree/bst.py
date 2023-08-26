# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def inorder_traversal_recursive(root) -> list[int]:
        res = []
        if not root:
            return [] 
        
        def dfs(root, res):
            if not root:
                return
            
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
            return

        dfs(root, res)        
        return res

    @staticmethod
    def inorder_traversal_iterative(root) -> list[int]:
        res = []
        if not root:
            return [] 
        
        curr, stack = root, []
    
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr:
                res.append(curr.val)
                curr = curr.right

        return res            

    @staticmethod
    def preorder_traversal_recursive(root) -> list[int]:
        res = []
        if not root:
            return []
        
        def dfs(root, res):
            if not root:
                return
            
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)

            return
        
        dfs(root, res)
        return res

    
    @staticmethod
    def preorder_traversal_iterative(root) -> list[int]:
        res = []
        if not root:
            return []

        curr, stack = root, []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

        return res
    
    @staticmethod
    def postorder_traversal_recursive(root) -> list[int]:
        res = []
        if not root:
            return res

        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
        
        dfs(root, res)
        return res

    @staticmethod  
    def postorder_traversal_iterative(root) -> list[int]:
        if not root:
            return []

        res = []
        stack = [(root, False)]

        while stack:
            curr, v = stack.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))
        
        return res

# bst matches tree in tree_traversal.md
bst = TreeNode(1)
bst.left = TreeNode(2)
bst.right = TreeNode(3)
bst.left.left = TreeNode(4)
bst.left.right = TreeNode(5)
bst.right.left = TreeNode(6)
bst.right.right = TreeNode(7)

print(f'Inorder   Traversal Recursive: {TreeNode.inorder_traversal_recursive(bst)}')
print(f'Inorder   Traversal Iterative: {TreeNode.inorder_traversal_iterative(bst)}')
print(f'Preorder  Traversal Recursive: {TreeNode.preorder_traversal_recursive(bst)}')
print(f'Preorder  Traversal Iterative: {TreeNode.preorder_traversal_iterative(bst)}')
print(f'Postorder Traversal Recursive: {TreeNode.postorder_traversal_recursive(bst)}')
print(f'Postorder Traversal Iterative: {TreeNode.postorder_traversal_iterative(bst)}')