class Solution:
    def minPathSum(self, grid):
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Iterate through the grid to calculate the minimum path sum
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue  # Skip the starting cell
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]  # Only move right
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]  # Only move down
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])  # Choose the minimum path
            
        # The bottom-right cell contains the minimum path sum
        return grid[m - 1][n - 1]
