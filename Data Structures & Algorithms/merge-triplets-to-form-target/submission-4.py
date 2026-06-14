class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        ans = None
        x,y,z = target
        for i in range(n):
            a,b,c = triplets[i]

            if ans is not None:
                A,B,C = ans
            if ans is None and a<=x and b<=y and c<=z:
                ans = triplets[i]
            elif ans and max(a,A)<=x and max(b,B)<=y and max(c,C)<=z:
                ans = [max(a,A),max(b,B),max(c,C)]
            if ans == target:
                return True
            print(ans,i)
        return False

#[15,9,8],[2,4,4],[2,6,1],[10,9,4],[10,4,1],[2,12,11],[1,4,2],[15,1,14],[6,2,9],[4,5,11]]
        