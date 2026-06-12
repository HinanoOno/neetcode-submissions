import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or stack[-1]<nums[i]:
                stack.append(nums[i])
            else:
                idx = bisect.bisect_left(stack,nums[i])
                stack[idx] = nums[i]
        return len(stack)
# [10,9,3,5,3,7,101,18]
# [3,5,7,9]