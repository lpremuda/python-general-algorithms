#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

import unittest

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
    ]

edges2 = [
    ['a', 'c'],
    ['a', 'b'],
    ['c', 'b'],
    ['c', 'd'],
    ['b', 'd'],
    ['e', 'd'],
    ['g', 'f']
    ]

debug = False

def shortest_path(edges: list[list[str]], src, dest) -> int:
    graph = build_graph(edges)
    shortest_distance = explore_bfs(graph, src, dest)
    return shortest_distance
    
def explore_bfs(graph, src, dest) -> int:
    queue = [(src, 0)]
    visited = set()
    while len(queue) > 0:
        # pop off element from end of queue
        curr_node, curr_dist = queue.pop(-1)
        if debug:
            print(f'curr_node=\'{curr_node}\', curr_dist={curr_dist}')
        if curr_node not in visited:
            visited.add(curr_node)
            if curr_node == dest:
                return curr_dist
            else:
                for neighbor in graph[curr_node]:
                    queue.insert(0, (neighbor, curr_dist+1))
             
    # -1 signifies that there is no path between src and dest
    return -1
    
def build_graph(edges: list[list[str]]) -> dict:
    graph = {}
    for edge in edges:
        a, b = edge[0:2]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
            
        graph[a].append(b)
        graph[b].append(a)
    
    return graph
    

class ConnectedComponentsCountTestCase(unittest.TestCase):

    def test_shortest_path(self):
        self.assertEqual(shortest_path(edges, 'w', 'z'), 2)
        self.assertEqual(shortest_path(edges, 'w', 'v'), 1)
        self.assertEqual(shortest_path(edges, 'w', 'w'), 0)
        self.assertEqual(shortest_path(edges, 'x', 'v'), 2)
        
    def test_return_minus1_when_no_path(self):
        self.assertEqual(shortest_path(edges2, 'b', 'g'), -1)
        

if __name__ == '__main__':    
    unittest.main()
    
    print('\nedges:')
    [print(edge) for edge in edges]
    graph = build_graph(edges)
    
    print('\ngraph:')
    [print(f'{k}: {v}') for k, v in graph.items()]
    print()