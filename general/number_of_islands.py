'''
200. NUMBER OF ISLANDS
https://leetcode.com/problems/number-of-islands/

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        self.printGrid(grid)
        print()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i,j)
                    count += 1

        self.printGrid(grid)
        return count



    def dfs(self, grid, i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        
        grid[i][j] = "#"
        
        self.dfs(grid, i-1, j)
        self.dfs(grid, i  , j+1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i  , j-1)

    def printGrid(self, grid) -> None:
        for row in grid:
            print(row)

s = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(s.numIslands(grid))
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))
