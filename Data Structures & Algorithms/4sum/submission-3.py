class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n-3):
            if i>=1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                cur = nums[i]+nums[j]
                l,r = j+1,n-1
                print(nums[i],nums[j],cur)
                while l<r:
                    tmp=nums[l]+nums[r]
                    if (cur+tmp)==target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        while l<n and nums[l-1]==nums[l]:
                            l+=1
                    elif cur+tmp>target:
                        r-=1
                    else:
                        l+=1
        return ans