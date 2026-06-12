class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            n = len(s)
            ans += str(n)+"#"+s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        m = len(s)
        while i<m:
            tmp = 0
            if s[i].isdigit():
                while s[i].isdigit():
                    tmp = tmp*10+int(s[i])
                    i+=1
                n = tmp
                word = s[i+1:i+n+1]
                ans.append(word)
                i = i+n+1 
            else:
                i += 1
            print(i,word)       
        return ans