class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n= len(s)
        l = 0
        ans = 0
        max_v = 0
        cnt = Counter()
        for i in range(n):
            cnt[s[i]]+=1
            max_v = max(max_v,cnt[s[i]])

            if (i-l+1)-max_v>k:
                while (i-l+1)-max_v>k:
                    cnt[s[l]]-=1
                    l+=1
            ans = max(ans,i-l+1)
            print(ans,l)
        return ans