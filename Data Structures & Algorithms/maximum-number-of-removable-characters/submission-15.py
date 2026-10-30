class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def check(mid):
            dat = set(removable[:mid])
            cur = ""
            cnt = 0
            for i in range(len(s)):
                if i in dat:
                    continue
                else:
                    if s[i] == p[cnt]:
                        cnt+=1
                    if cnt==len(p):
                        return True
            return False
            
        if not removable:
            return 0
        l,r = 0,len(removable)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l= mid+1
            else:
                r =mid-1
            #print(l,r,mid,ans)
        return ans