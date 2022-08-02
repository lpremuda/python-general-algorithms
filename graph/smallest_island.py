#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 13:39:58 2022

@author: lucas.premuda
"""

import sys
import unittest

grid = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W']
        ]

grid2 = [
        ['W', 'L', 'W', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'L', 'W'],
        ['W', 'L', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W', 'W']
        ]

grid_no_land = [
        ['W', 'W'],
        ['W', 'W'],
        ]

grid_all_land = [
        ['L', 'L', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'L', 'L']
        ]

grid_equal_sized_islands = [
        ['L', 'W', 'L', 'W', 'L'],
        ['L', 'W', 'L', 'W', 'L']
        ]

grid4 = [
        ['L', 'W', 'L', 'L', 'L'],
        ['L', 'L', 'L', 'W', 'L']
        ]


def smallest_island(grid: list[list[str]]) -> int: 
    def explore(grid, visited, row, col):
        if not is_valid_coordinate(row, col, num_rows, num_cols):
            return 0
        
        if f'{row},{col}' in visited:
            return 0
        
        visited.add(f'{row},{col}')
        
        
        if grid[row][col] == 'L':
            island_size = 1 + explore(grid,visited, row-1, col) + explore(grid,visited, row+1, col) + explore(grid,visited, row, col-1) + explore(grid,visited, row, col+1)
        elif grid[row][col] == 'W':
            return 0
        else:
            raise Exception("grid value was not land or water")
            
        return island_size
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    
    smallest = sys.maxsize
    visited = set()
    for i in range(num_rows):
        for j in range(num_cols):
            island_size = explore(grid, visited, i, j)
            if island_size > 0:
                print(f'Discovered island at {i},{j} of size {island_size}')
                smallest = min(smallest, island_size)
    
    # if still equal to maxsize, that means no islands were found
    if smallest == sys.maxsize:
        return 0
    else:
        return smallest
    
def is_valid_coordinate(row, col, num_rows, num_cols):
    return row >= 0 and row < num_rows and col >= 0 and col < num_cols
    

class SmallestIslandTestCase(unittest.TestCase):

    def test_island_count(self):
        self.assertEqual(smallest_island(grid), 2)
        self.assertEqual(smallest_island(grid2), 1)
        self.assertEqual(smallest_island(grid_no_land), 0)
        self.assertEqual(smallest_island(grid_all_land), 10)
        self.assertEqual(smallest_island(grid_equal_sized_islands), 2)
        self.assertEqual(smallest_island(grid4), 8)

if __name__ == '__main__': 
    unittest.main()
