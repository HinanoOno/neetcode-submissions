class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        data = defaultdict(int)
        for i in range(n):
            data[hand[i]]+=1
        hand.sort()
        if groupSize==1:
            return True
        for i in range(n):
            
            if data[hand[i]-1]>0 or data[hand[i]]==0:
                continue
            if data[hand[i]+1]>0:
                j = hand[i]+1
                data[hand[i]]-=1
                while data[j]>0:
                    data[j]-=1
                    j+=1
                    if j-hand[i]==groupSize:
                        break
                    
                if j-hand[i]<groupSize:
                    return False
            print(data)
        for d,v in data.items():
            if v>0:
                return False
        return True
                
                
