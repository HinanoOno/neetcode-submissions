class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                num = -nums[i]
            else:
                num = nums[i]
            if nums[num-1]<0:
                return num
            nums[num-1]*=-1
        return -1

# [-1,3,,2,2]
