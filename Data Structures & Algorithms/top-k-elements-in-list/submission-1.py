class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cnt = defaultdict(int)
        for i in range(n):
            cnt[nums[i]]+=1
        cur = []
        for i,v in cnt.items():
            cur.append([v,i])
        cur.sort(reverse = True)
        ans = []
        for i  in range(k):
            ans.append(cur[i][1])
        return ans
