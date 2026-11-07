class Solution:
    def romanToInt(self, s: str) -> int:
        data = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(s)
        ans = 0
        i = 0
        
        while i<n:
            if i+1<n:
                if s[i]=="I" and s[i+1] in ["V","X"]:
                    ans+=(data[s[i+1]])-1
                    i+=2
                elif s[i] == "X" and s[i+1] in ["L","C"]:
                    ans+=(data[s[i+1]])-10
                    i+=2
                elif s[i] == "C" and s[i+1] in ["D","M"]:
                    ans+=(data[s[i+1]])-100
                    i+=2
                else:
                    ans+=data[s[i]]
                    i+=1
            else:
                    ans+=data[s[i]]
                    i+=1
        return ans
        