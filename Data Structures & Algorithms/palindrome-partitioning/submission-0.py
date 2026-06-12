class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def dfs(cur,i):
            if i==n:
                ans.append(cur[:])
                return 
            for j in range(i,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    cur.append(s[i:j+1])
                    dfs(cur,j+1)
                    cur.pop()
        dfs([],0)
        return ans
    
    # aab dfs(a,1) dfs(aa,2) dfs(a,a)