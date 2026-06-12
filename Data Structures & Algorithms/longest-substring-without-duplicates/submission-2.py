class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cur = {}
        l = 0
        res = 0
        for i in range(n):
            if s[i] in cur:
                l = max(cur[s[i]]+1,l)
            cur[s[i]] = i
            res = max(res,i-l+1)
        return res

# zxyzxyz"
# cu={x,y,z}l=1