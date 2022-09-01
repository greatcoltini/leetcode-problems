class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # we are converting the grid to 0s because we have found a 1 connecting
        def turn_to_dust(i, j):
            if (i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0"):
                return
            grid[i][j] = "0"
            turn_to_dust(i, j + 1)
            turn_to_dust(i, j - 1)
            turn_to_dust(i + 1, j)
            turn_to_dust(i - 1, j)
            return

        res = 0

        # loop through the grid, if we encounter an island, kill all adjacent islands
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    turn_to_dust(i, j)


        return res