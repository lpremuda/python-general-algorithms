import unittest

# Refer to undirected_graph.jpg for illustration of graph

# Prompt: Given a undirected graph, source node, and destination node, determine
# if its possible (True or False) to go from source node to destination node

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
    ]

def undirected_path(edges: list[list[str]], src: str, dest: str) -> bool:
    graph = build_graph(edges)
    return has_path_dfs(graph, src, dest, set())

def build_graph(edges: list[list[str]]) -> dict:
    graph = {}
    
    for edge in edges:
        a = edge[0]
        b = edge[1]
        
        if a not in graph:
            graph[a] = []
        
        if b not in graph:
            graph[b] = []
            
        graph[a].append(b)
        graph[b].append(a)
    
    
    return graph

def has_path_dfs(graph: dict, src: str, dest: str, visited: set[str] = set()) -> bool:
    if src in visited:
        return False
    
    if src == dest:
        return True
    
    visited.add(src)
    
    for current in graph[src]:
        if has_path_dfs(graph, current, dest, visited):
            return True
        
    return False

class HasPathDFSTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print("Setting up DFS tests")

    # setUp is run before EVERY method in this class
    def setUp(self):
        print("Invoking setUp(self)...")
        self.has_path_func = undirected_path

    def test_has_path_dfs_returns_true(self):
        self.assertTrue(self.has_path_func(edges, 'i', 'k'))
        self.assertTrue(self.has_path_func(edges, 'k', 'l'))
        self.assertTrue(self.has_path_func(edges, 'l', 'm'))
        self.assertTrue(self.has_path_func(edges, 'm', 'i'))
        self.assertTrue(self.has_path_func(edges, 'o', 'n'))
        self.assertTrue(self.has_path_func(edges, 'n', 'o'))
        
    def test_has_path_dfs_returns_false(self):
        self.assertFalse(self.has_path_func(edges, 'o', 'l'))
        self.assertFalse(self.has_path_func(edges, 'n', 'k'))
        self.assertFalse(self.has_path_func(edges, 'm', 'o'))
        self.assertFalse(self.has_path_func(edges, 'n', 'l'))


if __name__ == '__main__':
    print('edges:')
    [print(edge) for edge in edges]
    graph = build_graph(edges)
    
    print('\ngraph:')
    [print(f'{k}: {v}') for k, v in graph.items()]
    print()
    
    unittest.main()
