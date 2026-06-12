class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range((n-2+1)//2+1):
            for j in range(n):
                matrix[i][j],matrix[n-1-i][j] = matrix[n-1-i][j],matrix[i][j]
        print(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                    
            print(matrix)
[7,8,9] 
[4,5,6]
[1,2,3]
