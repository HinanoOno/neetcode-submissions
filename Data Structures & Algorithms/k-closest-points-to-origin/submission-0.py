class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        def calc_dis(x,y):
            return math.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2) 
        data = []
        f = [0,0]
        for i in range(n):
            dis = calc_dis(f,points[i])
            data.append([dis,points[i]])
        data.sort()
        ans = []
        for i in range(k):
            ans.append(data[i][1])
        return ans

        