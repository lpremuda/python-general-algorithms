#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

# NOTE: THIS FILE IS CURRENTLY NOT WORKING
# I was playing around with using num_nodes (an int) asa global variable
# I believe int is a "pass by value" and not "pass by reference", so its
# tough to add one to the value and keep the value stable

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
    def explore(graph, node, visited, stack_depth) -> bool:
        global num_nodes
        stack_depth += 1
        tabs = '\t' * stack_depth
        print(f'{tabs}Exploring {node}')
        if node in visited:
            print(f'{tabs}{node} already explored, returning num_nodes={num_nodes}')
            return False
        
        print(f'{tabs}Adding {node} to visited')
        visited.add(node)
        
        num_nodes += 1
        print(f'{tabs}Incremented num_nodes to {num_nodes}')
        
        for neighbor in graph[node]:
            explore(graph, neighbor, visited, stack_depth)
            
        return True
    
    largest = 0
    
    visited = set()
    for node in graph.keys():
        print(f'Iterating on node = {node}')
        # reset num_nodes to 0 for each iteration
        num_nodes = 0
        stack_depth = 0
        # if returns True, exploration was done, so num_nodes is > 0
        if explore(graph, node, visited, stack_depth):
            print('Finished exploring, explore returned True')
            print(f'num_nodes = {num_nodes}')
            largest = max(largest, num_nodes)
    
    return largest



# class ConnectedComponentsCountTestCase(unittest.TestCase):

#     def test_3_connected_components(self):
#         self.assertEqual(connected_components_count(edges), 3)
        
#     def test_2_connected_components(self):
#         self.assertEqual(connected_components_count(edges2), 2)
        
#     def test_1_connected_components(self):
#         self.assertEqual(connected_components_count(edges3), 1)

if __name__ == '__main__':    
    print('graph:')
    [print(f'{k}: {v}') for k, v in graph.items()]
    print('')
    
    print(largest_component(graph))
    
    # unittest.main()