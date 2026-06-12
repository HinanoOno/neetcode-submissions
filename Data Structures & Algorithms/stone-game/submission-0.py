class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        a,b = 0,0
        flg = False
        for i in range(n):
            if not flg:
                if piles[0]<piles[-1]:
                    num = piles.pop()
                    a += num
                else:
                    num = piles.pop(0)
                    a += num
            else:
                if piles[0]<piles[-1]:
                    num = piles.pop()
                    b += num
                else:
                    num = piles.pop(0)
                    b += num
        return True if a>b else False


        