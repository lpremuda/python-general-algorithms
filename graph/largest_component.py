#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

import unittest

graph = {
    '0': ['1', '5', '8'],
    '1': ['0'],
    '2': ['3', '4'],
    '3': ['2', '4'],
    '4': ['2', '3'],
    '5': ['0', '8'],
    '8': ['0', '5']
    }

def largest_component(graph: dict) -> int:
    largest = 0
    
    visited = set()
    for node in graph.keys():
        print(f'Iterating on node = {node}')
        # reset num_nodes to 0 for each iteration
        num_nodes = 0
        stack_depth = 0
        # if returns True, exploration was done, so num_nodes is > 0
        num_nodes = explore(graph, node, visited, num_nodes, stack_depth)
        if num_nodes > 0:
            print('\tFinished exploring and num_nodes > 0')
            print(f'\tnum_nodes = {num_nodes}')
            largest = max(largest, num_nodes)
    
    return largest

def explore(graph, node, visited, num_nodes, stack_depth) -> int:
    stack_depth += 1
    tabs = '\t' * stack_depth
    print(f'{tabs}Exploring {node}')
    if node in visited:
        print(f'{tabs}{node} already explored, returning num_nodes={num_nodes}')
        return num_nodes
    
    print(f'{tabs}Adding {node} to visited')
    visited.add(node)
    
    num_nodes += 1
    print(f'{tabs}Incremented num_nodes to {num_nodes}')
    
    for neighbor in graph[node]:
        num_nodes = explore(graph, neighbor, visited, num_nodes, stack_depth)
        
    return num_nodes
    

class ConnectedComponentsCountTestCase(unittest.TestCase):

    def test_largest_component(self):
        self.assertEqual(largest_component(graph), 4)


if __name__ == '__main__':    
    print('graph:')
    [print(f'{k}: {v}') for k, v in graph.items()]
    print('')
        
    unittest.main()