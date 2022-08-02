import unittest

# Refer to directed_graph.jpg for illustration of graph

# Prompt: Given a directed graph, source node, and destination node, determine
# if its possible (True or False) to go from source node to destination node

directed_graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


def has_path_dfs(graph: dict, src: str, dest: str) -> bool:
    if src == dest:
        return True
    
    for current in graph[src]:
        if has_path_dfs(graph, current, dest):
            return True
        
    return False


def has_path_bfs(graph: dict, src: str, dest: str) -> bool:
    queue = [src]
    
    while len(queue) > 0:
        # pop off from end of queue
        current = queue.pop(-1)
        
        if current == dest:
            return True
        
        # add neighbors to queue
        for neighbor in graph[current]:
            queue.insert(0, neighbor)
        
    return False


class HasPathDFSTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print("Setting up DFS tests")

    # setUp is run before EVERY method in this class
    def setUp(self):
        print("Invoking setUp(self)...")
        self.has_path_func = has_path_dfs

    def test_has_path_dfs_returns_true(self):
        self.assertTrue(self.has_path_func(directed_graph, 'f', 'g'))
        self.assertTrue(self.has_path_func(directed_graph, 'f', 'i'))
        self.assertTrue(self.has_path_func(directed_graph, 'f', 'h'))
        self.assertTrue(self.has_path_func(directed_graph, 'f', 'k'))
        
    def test_has_path_dfs_returns_false(self):
        self.assertFalse(self.has_path_func(directed_graph, 'f', 'j'))
        
    def test_h_and_k_has_no_path_dfs(self):
        srcs = ['h', 'k']
        for src in srcs:
            keys: set[str] = set(directed_graph.keys())
            keys.remove(src)
            
            for dest in keys:
                self.assertFalse(self.has_path_func(directed_graph, src, dest))


class HasPathBFSTestCase(HasPathDFSTestCase):
        
    @classmethod
    def setUpClass(self):
        print("Setting up BFS tests")
    
    # setUp is run before EVERY method in this class
    def setUp(self):
        print("Invoking setUp(self)...")
        self.has_path_func = has_path_bfs


if __name__ == '__main__':
    unittest.main()
