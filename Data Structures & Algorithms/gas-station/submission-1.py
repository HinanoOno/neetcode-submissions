class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        if sum(gas)<sum(cost):
            return -1
        cur = 0
        ans = 0
        for i in range(n):
            cur +=(gas[i]-cost[i])
            if cur<0:
                cur = 0
                ans = i+1
        return ans



# gas = [1,2,3,4], cost = [2,2,4,1]
# cur= 4, 4 4 3,1