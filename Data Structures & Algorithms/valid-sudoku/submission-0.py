class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board),len(board[0])
        row = [[False]*10 for i in range(n)]
        col = [[False]*10 for i in range(m)]

        for i in range(n):
            for j in range(m):
                if board[i][j] !=".":
                    if row[i][int(board[i][j])] == True:
                        #print(row[i],board[i][j])
                        return False
                    else:
                        row[i][int(board[i][j])] = True
                    if col[j][int(board[i][j])] == True:
                        #print(col[j],board[i][j],i,j)
                        return False
                    else:
                        col[j][int(board[i][j])] = True

        for i in range(0,n-2,3):
            for j in range(0,m-2,3):
                cur = set()
                for x,y in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]:
                    rx,ry = i+x,j+y
                    if board[rx][ry]==".":
                        continue
                    if board[rx][ry] in cur:
                        return False
                    cur.add(board[rx][ry])
                    
        return True


# [[F,F,F,F,F]]  