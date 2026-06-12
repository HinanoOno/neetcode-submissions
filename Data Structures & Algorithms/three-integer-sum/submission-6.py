class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        for  i in range(n-2):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,n-1
            while l<r:
                cur=nums[i]+ nums[l]+nums[r]
                if cur==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l+1<n and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                elif cur<0:
                    while l+1<n and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                else:
                    while r-1>=0 and nums[r]==nums[r-1]:
                        r-=1
                    r-=1

        return ans
# [-4,-1,-1,-1,0,1,2]
# -4, l,r = 5,6
# -1 l,r = 2,6 [-,1-1,2]
# ,
            
        