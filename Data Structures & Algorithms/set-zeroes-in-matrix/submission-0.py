class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        col = set()
        row = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col.add(i)
                    row.add(j)
        for i in range(m):
            for j in range(n):
                if i in col or j in row:
                    matrix[i][j] = 0
                    