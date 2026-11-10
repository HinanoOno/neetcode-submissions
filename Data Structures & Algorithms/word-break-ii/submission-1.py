class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)

        n = len(s)
        ans = []
        def dfs(cur,i):
            #print(cur,i)
            nonlocal ans
            if i==n:
                ans.append(" ".join(cur))
            for word in wordset:
                    l = len(word)
                    if s[i:i+l] == word:
                        dfs(cur+[word],i+l)
        dfs([],0)
        return ans
        