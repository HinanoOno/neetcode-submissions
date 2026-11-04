class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        ans = 2**n-1
        cnt = 0
        l,r = 0,n-1
        while l<=r:
            if nums[l]+nums[r]>target:
                cnt+=2**(r-l)
                r-=1
            else:
                l+=1
            #print(l,r,cnt)
        print(ans,cnt)
        return (ans-cnt)%MOD

        