class CountSquares:

    def __init__(self):
        self.data = defaultdict(lambda:defaultdict(int))    

    def add(self, point: List[int]) -> None:
        rx,ry = point[0],point[1] 
        self.data[rx-1][ry-1] += 1
    
    def count(self, point: List[int]) -> int:
        rx,ry = point[0]-1,point[1] -1
        print(self.data)
        res = 0
        for y2 in self.data[rx]:
            side = y2-ry
            if side==0:
                continue
            x3,x4 = rx+side,rx-side
            res += (self.data[rx][y2] * self.data[x3][ry] *
                    self.data[x3][y2])

            res += (self.data[rx][y2] * self.data[x4][ry] *
                    self.data[x4][y2])
        return res

        