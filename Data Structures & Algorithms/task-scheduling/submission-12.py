class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        cnt = Counter(tasks)
        max_freq = cnt.most_common(1)[0]
        ch,val = max_freq
        max_freq_count = 0
        for i,v in cnt.items():
            if v==val:
                max_freq_count+=1
        return max((val-1)*(n+1)+max_freq_count,len(tasks))

                
#(max_freq-1)*(n+1) + max_freq_count
# (2-1)*2 + 2 = 5
# (2)*4 +1 - 9

