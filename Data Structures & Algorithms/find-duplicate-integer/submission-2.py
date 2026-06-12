class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = set(nums)
        for i in range(n):
            if nums[i] in set_nums:
                set_nums.remove(nums[i])
            else:
                return nums[i]