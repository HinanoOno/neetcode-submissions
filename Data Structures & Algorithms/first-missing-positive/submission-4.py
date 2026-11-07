class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        for ch in nums:
            if ch<=0:
                continue
            else:
                ans|=(1<<ch)
        max_v = max(nums)
        for i in range(1,max_v+1):
            if not ans&(1<<i):
                return i
        return max(1,max_v+1)

            