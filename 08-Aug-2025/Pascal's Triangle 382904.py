# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prev_Rows = self.generate(numRows - 1)
        new_Row = [1] * numRows
        
        for i in range(1, numRows - 1):
            new_Row[i] = prev_Rows[-1][i - 1] + prev_Rows[-1][i]
        
        prev_Rows.append(new_Row)
        return prev_Rows