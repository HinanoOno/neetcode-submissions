class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #print(start^goal)
        return bin(start^goal).count("1")
