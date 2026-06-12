class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone = -heapq.heappop(stones)

            stone2 = -heapq.heappop(stones)
            print(stone,stone2)
            if stone<stone2:
                heapq.heappush(stones,stone-stone2)
            elif stone>stone2:
                heapq.heappush(stones,stone2-stone)
            print(stones)
        
        return -stones[0] if stones else 0