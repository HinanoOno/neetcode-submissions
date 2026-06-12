class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        i = 0
        ans = []
        num = cnt.most_common()
        while i<k:
            ans.append(num[i][0])
            i+=1
        return ans