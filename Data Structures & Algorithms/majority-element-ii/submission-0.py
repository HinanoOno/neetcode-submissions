class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_v = len(nums)/3
        ans = []
        cnt = Counter(nums)
        for i,v in cnt.items():
            if v>max_v:
                ans.append(i)
        return ans