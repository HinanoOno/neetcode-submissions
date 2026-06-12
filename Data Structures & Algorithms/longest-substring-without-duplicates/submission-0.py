class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cur = set()
        l = 0
        ans = 0
        for i in range(n):
            if s[i] in cur:
                while s[i] in cur:
                    cur.remove(s[l])
                    l+=1
            ans = max(ans,i-l+1)  
            cur.add(s[i])  
        return ans

# zxyzxyz"
# cu={x,y,z}l=1