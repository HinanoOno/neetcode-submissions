class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque([])
        ans = []
        for i in range(n):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)

            if i-k+1>=0 and q[0]>=i-k+1:
                ans.append(nums[q[0]])
            else:
                if i-k+1<0:
                    continue
                while q[0]<i-k+1:
                    q.popleft()
                ans.append(nums[q[0]])
        return ans

        


        


