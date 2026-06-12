class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[0]
        for i in range(1,n):
            cur ^= nums[i]
            print(cur)
        return cur
        