#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

import unittest

# grid represents the illustration in island_count.jpg
grid = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'L', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W']
        ]

grid2 = [
        ['W', 'L', 'W', 'L', 'L', 'L']
        ]

grid3 = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
        ]

def island_count(grid: list[list[str]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    num_islands = 0
    
    visited = set() 
    
    for i in range(num_rows):
        for j in range(num_cols):
            if f'{i},{j}' not in visited:
                if grid[i][j] == 'L':
                    print(f'Land discovered at ({i},{j})')
                    # an island has been found, so increment num_islands
                    num_islands += 1
                    print(f'Incremented num_islands to {num_islands}')
                    # explored to mark other land nodes visited
                    explore_dfs(grid, i, j, visited, num_rows, num_cols)
                
                
    return num_islands
    
def explore_dfs(grid, row, col, visited, num_rows, num_cols):
    row_inc = [-1, 1, 0, 0]
    col_inc = [0, 0, -1, 1]
    
    for i in range(len(row_inc)):
        new_row = row + row_inc[i]
        new_col = col + col_inc[i]
        if is_valid_coordinate(new_row, new_col, num_rows, num_cols) and f'{new_row},{new_col}' not in visited:
            # mark as visited
            visited.add(f'{new_row},{new_col}')
            # if new node is land, continue the DFS traversal
            if grid[new_row][new_col] == 'L':
                explore_dfs(grid, new_row, new_col, visited, num_rows, num_cols)
            
def is_valid_coordinate(row, col, num_rows, num_cols):
    return row >= 0 and row < num_rows and col >= 0 and col < num_cols

class IslandCountTestCase(unittest.TestCase):

    def test_island_count(self):
        self.assertEqual(island_count(grid), 4)
        self.assertEqual(island_count(grid2), 2)
        self.assertEqual(island_count(grid3), 3)
        

if __name__ == '__main__':    
    unittest.main()
