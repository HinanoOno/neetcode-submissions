class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        data = set()
        for i in ["a","e","i","o","u"]:
            data.add(i)
        dp = [0]*n
        for i in range(n):
            w = words[i]
            if w[0] in data and w[-1] in data:
                dp[i] += 1
        for i in range(1,n):
            dp[i] += dp[i-1]
        print(dp)
        ans = []
        for i in range(len(queries)):
            l,r = queries[i]
            if l-1<0:
                ans.append(dp[r])
            else:
                ans.append(dp[r]-dp[l-1])
        return ans



        