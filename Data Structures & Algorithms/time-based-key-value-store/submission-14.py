class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp,value))
        else:
            self.data[key] = [(timestamp,value)  ]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            cand = self.data[key]
            cand.sort()
            print(cand)
            if cand[0][0]>timestamp:
                return ""
            l,r = 0,len(cand)
            while (r-l)>1:
                mid = (l+r)//2
                if cand[mid][0]<=timestamp:
                    l = mid
                else:
                    r = mid
            return cand[l][1]
        else:
            return ""
        
