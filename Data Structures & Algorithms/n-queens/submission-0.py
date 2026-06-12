class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = [False] * n
        dia1 = [False] * (2 * n - 1) # 右上がり: row + col
        dia2 = [False] * (2 * n - 1) # 右下がり: row - col + n - 1
        def track(row):

            if row == n:
                res.append(["".join(r) for r in board])
                print(res)
                return
            for col in range(n):
                if cols[col] or dia1[row-col+n-1] or dia2[row+col]:
                    continue
                cols[col] = True
                dia1[row-col+n-1] = True
                dia2[row+col] = True
                board[row][col] ="Q"
                track(row+1)
                board[row][col] ="."
                cols[col] = False
                dia1[row-col+n-1] = False
                dia2[row+col] = False

        track(0)
        return res