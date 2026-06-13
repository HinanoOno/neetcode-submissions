class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board),len(board[0])
        
        def dfs(x,y):
            for (dx,dy) in[(1,0),(0,1),(-1,0),(0,-1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=="O":
                    board[nx][ny] = "2"
                    dfs(nx,ny)
        for i in range(n):
            if board[i][0]=="O":
                board[i][0]="2"
                dfs(i,0)
            if board[i][m-1]=="O":
                board[i][m-1]="2"
                dfs(i,m-1)
        for i in range(m):
            if board[0][i]=="O":
                board[0][i]="2"
                dfs(0,i)
            if board[n-1][i]=="O":
                board[n-1][i]="2"
                dfs(n-1,i)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="2":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"