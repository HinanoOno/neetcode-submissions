class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = sum(nums)

        def check(mid):
            cnt = 1
            cur = 0
            for i in range(n):
                cur+=nums[i]
                if cur>mid:
                    cur = nums[i]
                    cnt+=1
            
            return True if cnt<=k else False

        l,r = max(nums),total+1
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
        