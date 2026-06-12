class Solution:
    def checkValidString(self, t: str) -> bool:
        n = len(t)
        memo = {}
        def dfs(cur,s,f):
            #print(cur,s,f,memo)
            if s<f:
                return False
            if cur==n:
                return True if s==f else False
            if (cur,s,f) in memo:
                return memo[(cur,s,f)]
            elif cur>n:
                memo[(cur,s,f)] = False
                return False
            if t[cur]=="(":
                if dfs(cur+1,s+1,f):
                    memo[(cur+1,s+1,f)] = True
                    return True
            elif t[cur]==")":
                if dfs(cur+1,s,f+1):
                    memo[(cur+1,s,f+1)] = True
                    return True
            elif t[cur]=="*":
                if dfs(cur+1,s,f):
                    memo[(cur+1,s,f)] = True
                    return True
                if dfs(cur+1,s+1,f):
                    memo[(cur+1,s+1,f)] = True
                    return True
                if dfs(cur+1,s,f+1):
                    memo[(cur+1,s,f+1)] = True
                    return True
            memo[(cur,s,f)] = False
            return False
        return dfs(0,0,0)
                