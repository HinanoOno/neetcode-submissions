class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        data = defaultdict(int)
        for i in range(n):
            data[nums[i]] +=1
        print(data)
        ans = 1
        for i in range(n):
            print(data[nums[i]+1])
            if  data[nums[i]+1]>=1 and  not data[nums[i]-1]:
                cur = 1
                j = nums[i]+1
                while data[j]>0:
                    cur+=1
                    j+=1
                ans = max(ans,cur)
                print(cur)
        return ans