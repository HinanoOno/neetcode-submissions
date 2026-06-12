class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[l]

#  nums = [4,5,0,1,2,3]
# l,r = 0,5 mid = 2 r = 2
# l,r = 0,2 mid = 1l=2