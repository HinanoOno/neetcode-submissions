class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        cnt = Counter(s1)
        f = Counter(s2[:m])
        if cnt==f:
            return True
        for i in range(1,n-m+1):
            f[s2[i-1]]-=1
            if f[s2[i-1]]==0:
                del f[s2[i-1]]
            f[s2[i+m-1]] += 1
            if f==cnt:
                return True
        return False


# s1 = "abc" 3, s2 = "lecabee" 7
# {a,b,c} f={c,a} (3,7) 
