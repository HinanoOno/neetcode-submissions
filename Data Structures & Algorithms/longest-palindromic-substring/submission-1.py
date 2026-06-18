class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[1]*(n+1) for i in range(n+1)]

        def check(l,r):
            i,j = l,r
            while i-1>=0 and j+1<n:
                if s[i-1] == s[j+1]:
                    i-=1
                    j+=1
                else:    
                    break
            return (i,j)
        res = ""
        for i in range(n):
            ans = check(i,i)
            l,r = ans[0],ans[1]
            print(l,r,i)
            if (r-l+1)>len(res):
                res = s[l:r+1]
            ans2 = check(i,i+1)
            if i+1<n and s[i] == s[i+1]:
                l,r = ans2[0],ans2[1]
                print(l,r,i,i+1)
                if (r-l+1)>len(res):
                    res = s[l:r+1]
        return res



        