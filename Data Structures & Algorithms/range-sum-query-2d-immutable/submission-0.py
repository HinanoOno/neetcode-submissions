class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n,self.m = len(matrix),len(matrix[0])
        self.rows = [m for m in matrix]
        j = 0
        while j<self.n:
            for i in range(1,self.m):
                self.rows[j][i] += self.rows[j][i-1]
            j+=1
        print(self.rows)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        j = row1
        while j<=row2:
            if col1==0:
                ans+=self.rows[j][col2]
            else:
                ans+=self.rows[j][col2]-self.rows[j][col1-1]
            j+=1
        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)