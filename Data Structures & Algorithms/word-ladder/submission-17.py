class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList= set(wordList)
        if beginWord==endWord:
            return 0
        if endWord not in wordList:
            return 0
        ans = float('inf')
        q = deque([(1,beginWord)])
        while q:
            cnt,cur = q.popleft()
            if cur==endWord:
                return cnt
            for j in range(len(cur)):
                for i in range(26):
                    ch = chr(ord("a")+i)
                    nex = cur[:j] + ch + cur[j+1:]
                    if nex in wordList:
                        wordList.remove(nex)
                        q.append((cnt+1,nex))
        return 0
    
                    
        