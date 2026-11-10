class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ans = 0
        def dfs(j,yoko,tate,naname,naname2):
            nonlocal ans
            if j==n:
                ans += 1
                return 
            for i in range(n):
                if i not in yoko and j not in tate and (j-i) not in naname and (j+i) not in naname2:
                    yoko.add(i)
                    tate.add(j)
                    naname.add(j-i)
                    naname2.add(j+i)
                    dfs(j+1,yoko,tate,naname,naname2)
                    yoko.remove(i)
                    tate.remove(j)
                    naname.remove(j-i)
                    naname2.remove(j+i)
            return 
        
        yoko = set()
        tate,naname,naname2 = set(),set(),set()
        dfs(0,yoko,tate,naname,naname2)
        return ans
