class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def dfs(i,j,cur):
            print(i,j,cur)
            if cur == len(word):
                return True
            for rx,ry in [(1,0),(0,1),(0,-1),(-1,0)]:
                nx,ny = i+rx,j+ry
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == word[cur]:
                    tmp = board[nx][ny]
                    board[nx][ny] = "."
                    if dfs(nx,ny,cur+1):
                        return True
                    board[nx][ny] = tmp
            return False

        for i in range(n):
            for j in range(m):
               if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = "."
                    if dfs(i,j,1):
                        return True
                    board[i][j] = tmp
        return False