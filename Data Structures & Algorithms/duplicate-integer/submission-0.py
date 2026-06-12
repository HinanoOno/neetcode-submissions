class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i  in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        