class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)
        data = Counter()
        cur = 1
        ans,tmp = [],set()
        for ch in s:
            data[ch]+=1
            tmp.add(ch)
            if data[ch]==cnt[ch]:
                tmp.remove(ch)
                if len(tmp)==0:
                    ans.append(cur)
                    cur = 1
                    continue
                
            cur += 1
        return ans
        