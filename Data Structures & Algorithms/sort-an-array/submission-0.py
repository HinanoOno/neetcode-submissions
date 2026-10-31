import random
import sys
sys.setrecursionlimit(20000)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        def sort(nums):
            print(nums)
            m = len(nums)
            if m<=1:
                return nums
            pivot = random.randint(0,m-1)
            l,r = [],[]
            mid = []
            for i in range(m):
                if nums[i]<nums[pivot]:
                    l.append(nums[i])
                elif nums[i] == nums[pivot]:
                    mid.append(nums[i])
                else:
                    r.append(nums[i])
            l_n,r_n = [],[]
            if l:
                l_n = sort(l)
            if r:
                r_n = sort(r)

            return l_n+mid+r_n
        return sort(nums)
        