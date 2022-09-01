class Solution(object):
    def pacificAtlantic(self, heights):
        len_rows, len_cols = len(heights), len(heights[0])

        # perform depth first search, creating paths where we can traverse
        def dfs(i, j, prev_height, visited_cells):
            if i < 0 or i == len_rows or j < 0 or j == len_cols:
                # out of bounds
                return

            if (i, j) in visited_cells:
                # already visited
                return

            height = heights[i][j]

            if height < prev_height:
                # water can't flow to a higher height
                return

            # ocean is reachable from current coordinate
            visited_cells.add((i, j))

            # all four directions
            dfs(i + 1, j, height, visited_cells)
            dfs(i - 1, j, height, visited_cells)
            dfs(i, j + 1, height, visited_cells)
            dfs(i, j - 1, height, visited_cells)

        pacific_coords = set()

        # top row
        for j in range(len_cols):
            dfs(0, j, 0, pacific_coords)

        # left col
        for i in range(len_rows):
            dfs(i, 0, 0, pacific_coords)

        atlantic_coords = set()

        # right col
        for i in range(len_rows):
            dfs(i, len_cols - 1, 0, atlantic_coords)

        # bottom row
        for j in range(len_cols):
            dfs(len_rows - 1, j, 0, atlantic_coords)

        # intersection of coords reachable from both Pacific and Atlantic
        return list(pacific_coords & atlantic_coords)


print(Solution().pacificAtlantic([[1,2,2,3,5],
                                  [3,2,3,4,4],
                                  [2,4,5,3,1],
                                  [6,7,1,4,5],
                                  [5,1,1,2,4]]))





"""
-- go through each cell in matrix and determine if it can approach atlantic or pacific

TRACK?
- visited ? reach ATL or reach PAC

1. check all touching cells if they can go to atlantic or pacific
2. if they can and current cell >= them, then current cell can
3. if unknown, recurse
4. if can't, check all other cells, if can't, pass




"""