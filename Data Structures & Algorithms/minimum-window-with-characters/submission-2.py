class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        n,m = len(s),len(t)
        t_set = set(t)
        t_count = Counter(t)
        cnt = set()
        data = Counter()
        have,need = 0,len(t_set)
        l = 0
        ans = (0,float('inf'))
        
        for r in range(n):
            c= s[r]
            data[c]+=1

            if c in t_set and t_count[c] == data[c]:
                have += 1
            while have ==need:
                if (r-l+1)<ans[1]-ans[0]+1:
                    ans = (l,r)
                data[s[l]]-=1
                if s[l] in t_set and data[s[l]]<t_count[s[l]]:
                    have -= 1
                l += 1
            print(data)
        l,r = ans
        return s[l:r+1] if ans[1]!=float('inf') else ""