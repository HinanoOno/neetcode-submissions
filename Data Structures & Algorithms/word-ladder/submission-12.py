class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if beginWord==endWord or endWord not in wordList:
            return 0
        
        q = deque([(beginWord,1)])
        while q:
            cur,cnt = q.popleft()
            if cur==endWord:
                return cnt
            for i in range(len(cur)):
                for j in range(97,123):
                    word = cur[:i] + chr(j) + cur[i+1:]
                    if word in wordList:
                        wordList.remove(word) # ここで削除して再訪問を防
                        q.append((word,cnt+1))
        return 0



        