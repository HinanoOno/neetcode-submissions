class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n= len(s)
        l = 0
        cnt = Counter()
        max_ch = s[0]
        ans = 0
        for i in range(n):
            cnt[s[i]]+=1
            max_ch = cnt.most_common()[0]
            print(max_ch)
            ch,v = max_ch[0],max_ch[1]

       
            if (i-l+1)-v>k:
                while (i-l+1)-v>k:
                    cnt[s[l]]-=1
                    max_ch = cnt.most_common()[0]
                    ch,v = max_ch[0],max_ch[1]
                    l+=1
            ans = max(ans,i-l+1)
            print(ans,l)
            #print(i,l)
        return ans
#BAAA max_ch
# AA l,i=1,1