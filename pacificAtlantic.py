class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        reachOcean = [[]] # list of whether or not the cell has been visited; 0 = not visited, 1 = visited no exit,
        for i in range(len(heights)):
            for j in range(len(heights)):
                if self.canTouchOcean(heights[i][j], heights, i, j):
                    reachOcean.append([i, j])


    def canTouchOcean(self, height, heights, i, j):
        if i == 0 or j == 0 or i == len(heights) or j == len(heights):
            return True
        



"""
-- go through each cell in matrix and determine if it can approach atlantic or pacific

TRACK?
- visited ? reach ATL or reach PAC

1. check all touching cells if they can go to atlantic or pacific
2. if they can and current cell >= them, then current cell can
3. if unknown, recurse
4. if can't, check all other cells, if can't, pass




"""