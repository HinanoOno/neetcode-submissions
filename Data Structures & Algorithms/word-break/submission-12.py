class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(cur):
            nonlocal memo
            if cur=="":
                return True
            if cur in memo:
                return memo[cur]
            ans = False
            for w in wordDict:
                if cur.startswith(w):
                    if dfs(cur[len(w):]):
                        memo[cur] = True
                        return True
            memo[cur] = False
            return False
        return dfs(s)


# neet dfs(code)
