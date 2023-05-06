class Solution:
    def func(self,matrix,I,J):
        for j in range(len(matrix[0])):
            matrix[I][j]=0
        for i in range(len(matrix)):
            matrix[i][J]=0
        return matrix
    def find_idxs(self,matrix):
        row,col = set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        return row,col
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = self.find_idxs(matrix)
        for r in row:
            for c in col:
                matrix = self.func(matrix,r,c)