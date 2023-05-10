class Solution(object):
    
    def floorMod(self, x, y):
        """
        """
        return ((x % y) + y) % y

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # we need to generate nxn matrix, where it spirals into n2
        # i.e. n = 1 : [[1]]
        # n = 2 : [[1, 2], [4, 3]]
        # n = 3 : [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        result = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        direction = [[0, 1], [1,0], [0, -1], [-1, 0]]
        d = 0
        row = 0
        col = 0
        while (count <= n * n):
            result[row][col] = count
            count += 1
            r = self.floorMod(row + direction[d][0], n)
            c = self.floorMod(col + direction[d][1], n)
            
            if (result[r][c] != 0):
                d = (d + 1) % 4
            
            row += direction[d][0]
            col += direction[d][1]
        
        return result
    