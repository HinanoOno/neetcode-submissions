class TimeMap:

    def __init__(self):
        self.data =defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.data[key],(-timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.data[key])==0:
            return ""
        tmp = []
        while len(self.data[key])>0:
            time,val = heapq.heappop(self.data[key])
            tmp.append((time,val))

            if abs(time)<=timestamp:
                for t,v in tmp:
                    heapq.heappush(self.data[key],(t,v)) 
                return val

        for t,v in tmp:
            heapq.heappush(self.data[key],(t,v))
            print(self.data[key])
        return ""
        