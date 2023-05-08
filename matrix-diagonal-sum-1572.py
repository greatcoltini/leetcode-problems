class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        #primary matrix will sum up 0,0 to i,j where i==j==n 
        diagonal_sum = 0
        n = 0
        while n < len(mat[0]):
            diagonal_sum += mat[n][n]
            n += 1
        # for i in mat:
        #     for j in i:
        #         if i == j:
        #             diagonal_sum = j
        
        # secondary diagonal starts at (0, j) and increments as such:
        # (0 + 1, j - 1) + (0 + 2, j - 2) until j == 0
        # additionally, exclude mirror items (n, n)
        n = len(mat[0]) - 1
        counter = 0
        while counter <= n:
            if (counter != (n - counter)):
                diagonal_sum += mat[counter][n - counter]
            counter += 1
            
        return diagonal_sum
        