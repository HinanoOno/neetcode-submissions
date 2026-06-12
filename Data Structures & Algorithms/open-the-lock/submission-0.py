class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        q = deque([])
        q.append("0000")
        seen = set(deadends)
        if "0000" in seen:
            return -1
        seen.add("0000")
        steps = 0
        while q:
            steps += 1
            for i in range(len(q)):
                lock = q.popleft()
                print(lock)
                for j in range(4):
                    for k in[1,-1]:
                        digit = str((int(lock[j])+k+10)%10)  
                        nextLock = lock[:j] +digit+lock[j+1:] 
                        if nextLock in seen:
                            continue
                        if nextLock == target:
                            return steps
                        q.append(nextLock)
                        seen.add(nextLock)
        return -1 