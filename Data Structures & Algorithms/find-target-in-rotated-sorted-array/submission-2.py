class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r = mid-1
            else:
                if nums[l]<=target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
# [4,5,6,7,0,1,2]
# l,r = 0,6 mid=3
# L=4 r = 6 mid = 5
# r=4 l04