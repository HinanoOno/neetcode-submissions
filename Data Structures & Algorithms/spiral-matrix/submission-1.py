class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        top,bottom = 0,m-1
        left,right=0,n-1
        while top<=bottom and left<=right:
            for i  in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                    ans.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for j in range(bottom,top-1,-1):
                    ans.append(matrix[j][left])
                left+=1
            #print(ans,top,bottom,left,right)
        return ans



# [0,0] n=3
# i,j
# right->down->left->up->right...