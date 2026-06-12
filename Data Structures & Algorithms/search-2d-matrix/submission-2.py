class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        row = None
        for i in range(m-1):
            if matrix[i][0]<=target<matrix[i+1][0]:
                row = i
        row = m-1 if row is None else row
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid+1
            else:
                r = mid-1
        return False
# 
# l,r = 0,4
# mid = 2
# l,r = 0,1
# mid =0
# l=