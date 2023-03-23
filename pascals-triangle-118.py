class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = []
        for i in range(numRows):
            rows.append(self.genRow(i, rows))
        return rows

    # return a row of pascal
    def genRow(self, previousRow, rows):
        row = []
        i = 0

        if rows == []:
            return [1]
        
        while i < len(rows[previousRow]) + 1:
            if i == 0 or i == len(rows[previousRow]) + 1:
                row[i] = 1
            else:   
                row[i] = rows[previousRow][i-1] + rows[previousRow][i]
        return row