class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.val)
    
    def insert_node(self, value):
        if self.val is not None:
            if value < self.val:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert_node(value)
            elif value > self.val:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert_node(value)
    
    @staticmethod
    def insert_nodes(vals: list, root):
        for val in vals:
            root.insert_node(val)
    
    def bfs(self, root=None):
        if root is None:
            return

        # Initialize queue with the root node
        queue = [root]

        while len(queue) > 0:
            print(f'{queue}, ', end='')

            cur_node = queue.pop(0)

            print(f'{cur_node.val}, ', end='')

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
            
            print(f'{queue}')
            

root = Node(4)
root.insert_nodes([2, 1, 3, 6, 5, 7], root)
print(root)
print(root.left)
print(root.right)

print("BFS search")
root.bfs(root)
