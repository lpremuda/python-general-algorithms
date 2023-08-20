
class Solution:
    def __init__(self, dfs_direction):
        self.counter = 0
        self.grid = [
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X"],
        ]
        self.dfs_direction = dfs_direction
    
    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]) or self.grid[i][j] != "X":
            return

        # Mark node as explored with value
        self.grid[i][j] = str(self.counter)
        self.counter += 1

        match self.dfs_direction:
            case "CLOCKWISE_TOP":
                self.dfs(i-1, j)
                self.dfs(i  , j+1)
                self.dfs(i+1, j)
                self.dfs(i  , j-1)
            case "CLOCKWISE_RIGHT":
                self.dfs(i  , j+1)
                self.dfs(i+1, j)
                self.dfs(i  , j-1)
                self.dfs(i-1, j)
            case "CLOCKWISE_BOTTOM":
                self.dfs(i+1, j)
                self.dfs(i  , j-1)
                self.dfs(i-1, j)
                self.dfs(i  , j+1)
            case "CLOCKWISE_LEFT":
                self.dfs(i  , j-1)
                self.dfs(i-1, j)
                self.dfs(i  , j+1)
                self.dfs(i+1, j)
    
def printGrid(grid):
    for row in grid:
        print(row)
    print()

print("Clockwise - Top first")
s = Solution("CLOCKWISE_TOP")
s.dfs(0,0)
printGrid(s.grid)

gridSolution = [
    ["0", "1", "2", "3", "4"],
    ["17", "16", "11", "10", "5"],
    ["18", "15", "12", "9", "6"],
    ["19", "14", "13", "8", "7"],
]

print("Clockwise - Right first")
s = Solution("CLOCKWISE_RIGHT")
s.dfs(0,0)
printGrid(s.grid)

gridSolution = [
    ["0", "1", "2", "3", "4"],
    ["19", "18", "17", "16", "5"],
    ["12", "13", "14", "15", "6"],
    ["11", "10", "9", "8", "7"],
]

print("Clockwise - Bottom first")
s = Solution("CLOCKWISE_BOTTOM")
s.dfs(0,0)
printGrid(s.grid)

gridSolution = [
    ["0", "7", "8", "15", "16"],
    ["1", "6", "9", "14", "17"],
    ["2", "5", "10", "13", "18"],
    ["3", "4", "11", "12", "19"],
]

print("Clockwise - Left first")
s = Solution("CLOCKWISE_LEFT")
s.dfs(0,0)
printGrid(s.grid)

gridSolution = [
    ["0", "1", "2", "3", "4"],
    ["9", "8", "7", "6", "5"],
    ["10", "11", "12", "13", "14"],
    ["19", "18", "17", "16", "15"],
]