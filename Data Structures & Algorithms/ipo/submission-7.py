class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # [1,4,2,3]
        # [0,3,1,1]
        # [1,1,1,2]
        seen = set()
        min_v = None
        for i in range(n):
            if capital[i]<=w:
                seen.add(i)
                if not min_v or profits[i]>profits[min_v]:
                    min_v = i
        target = []
        total = 0
        for i,p in enumerate(profits):
            if i==min_v:
                continue
            c = capital[i]
            target.append([p,c,i])
            total += p
        target.sort(reverse=True)
        print(target)
        total = sum([p for p,c,i in target[:k-1]])
        flg = False
        if min_v is None:
            return w
        return total+profits[min_v]+w

        
        




