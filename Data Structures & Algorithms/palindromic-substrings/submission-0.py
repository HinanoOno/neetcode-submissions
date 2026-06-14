class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    ans += 1
        return ans

# s = "aaa"
# a,aa,aaa,a