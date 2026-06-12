class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]
            
            res = 1
            for ni, nj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ri, rj = i + ni, j + nj
                # 増加している場合のみ進む
                if 0 <= ri < n and 0 <= rj < m and matrix[ri][rj] > matrix[i][j]:
                    res = max(res, 1 + dfs(ri, rj))
            
            memo[(i, j)] = res
            return res

        # 全てのセルを起点に計算し、その最大値をとる
        max_path = 0
        for i in range(n):
            for j in range(m):
                max_path = max(max_path, dfs(i, j))
        
        return max_path