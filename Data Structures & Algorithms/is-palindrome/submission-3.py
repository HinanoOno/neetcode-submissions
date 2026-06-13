class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","")
        n = len(s)
        input = ""
        for i in range(n):
            if s[i].isalnum():
                input+=s[i]
        n = len(input)
        l,r = 0,n-1
        while l<r:
            if input[l]!=input[r]:
                return False
            l+=1
            r-=1
        return True
# tabacat
# 

        