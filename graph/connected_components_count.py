#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

# Refer to connected_components_count.jpg for illustration of graph
# Find the number of connected components in an edges data structure

import unittest

edges = [
    ['1', '2'],
    ['6', '4'],
    ['6', '5'],
    ['6', '7'],
    ['6', '8'],
    ['3', '3']
    ]

edges2 = [
    ['1', '2'],
    ['6', '4'],
    ['6', '5'],
    ['6', '7'],
    ['6', '8']
    ]

edges3 = [
    ['6', '4'],
    ['6', '5'],
    ['6', '7'],
    ['6', '8']
    ]

def connected_components_count(edges: list[list[str]]) -> int:
    # initialize count
    count = 0
    
    # convert list of edges to graph
    graph = build_graph(edges)
    
    visited = set()
    
    for current in graph.keys():
        # if explore returns True, all nodes in this DFS traversal have not been visited
        if explore(graph, current, visited):
            count += 1
            
    return count

def build_graph(edges: list[list[int]]) -> dict:
    graph = {}
    for edge in edges:
        a, b, = edge[:]
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        
        graph[a].add(b)
        graph[b].add(a)
    
    return graph

def explore(graph: dict, src: str, visited: set[str]) -> bool:
    # it matters only on the first "level" of this traversal if src has already
    # been visited
    if src in visited:
        return False
    
    visited.add(src)
    
    # continue to explore further down
    for neighbor in graph[src]:
        # do not capture return in a veriable because it doesn't matter whether
        # the return is True or False here
        explore(graph, neighbor, visited)
    
    return True

class ConnectedComponentsCountTestCase(unittest.TestCase):

    def test_3_connected_components(self):
        self.assertEqual(connected_components_count(edges), 3)
        
    def test_2_connected_components(self):
        self.assertEqual(connected_components_count(edges2), 2)
        
    def test_1_connected_components(self):
        self.assertEqual(connected_components_count(edges3), 1)

if __name__ == '__main__':    
    print('edges:')
    [print(edge) for edge in edges]
    graph = build_graph(edges)
    
    print('\ngraph:')
    [print(f'{k}: {v}') for k, v in graph.items()]
    print('')
    
    unittest.main()