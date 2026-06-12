class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = (l+r)//2

            row,col = (mid)//n, mid%(n)
            print(row,col,mid)
            if matrix[row][col] == target:
                return True
            if  matrix[row][col] < target:
                l = mid+1
            else:
                r = mid-1
        return False
# l,r = 0,1
# mid=0 row,col = 0,0