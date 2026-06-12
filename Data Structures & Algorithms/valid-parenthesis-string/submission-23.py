class Solution:
    def checkValidString(self, t: str) -> bool:
        n = len(t)
        memo = {}
        def dfs(cur,s):
            #print(cur,s,f,memo)
            if s<0:
                return False
            if cur==n:
                return True if s==0 else False
            if (cur,s) in memo:
                return memo[(cur,s)]
            elif cur>n:
                memo[(cur,s)] = False
                return False
            if t[cur]=="(":
                if dfs(cur+1,s+1):
                    memo[(cur+1,s+1)] = True
                    return True
            elif t[cur]==")":
                if dfs(cur+1,s-1):
                    memo[(cur+1,s-1)] = True
                    return True
            elif t[cur]=="*":
                if dfs(cur+1,s):
                    memo[(cur+1,s)] = True
                    return True
                if dfs(cur+1,s+1):
                    memo[(cur+1,s+1)] = True
                    return True
                if dfs(cur+1,s-1):
                    memo[(cur+1,s-1)] = True
                    return True
            memo[(cur,s)] = False
            return False
        return dfs(0,0)
                