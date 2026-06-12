class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        data = defaultdict(int)
        for i in range(n):
            
            if target-nums[i] in data:
                return [data[target-nums[i]],i]
            data[nums[i]] = i


# {3:0,4:}