class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or (beginWord!=endWord and endWord not in wordList)or len(beginWord)!=len(endWord):
            return 0
        
        n = len(wordList)
        data = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1,n):
                a,b = wordList[i],wordList[j]
                print(a,b,n)
                if len(a)!=len(b):
                    continue
                cnt = 0
                for k in range(len(a)):
                    if a[k]!=b[k]:
                        cnt+=1
                if cnt==1:
                    data[a].append(b)
                    data[b].append(a)
        print(data)
        q = deque([])
        seen = set()
        for i in range(n):
            a= wordList[i]
            if len(a)!=len(beginWord):
                continue
            cnt = 0
            for i in range(len(a)):
                if a[i]!=beginWord[i]:
                    cnt+=1
            if cnt==1:
                q.append((1,a))
                seen.add(a)
        while q:   
            cur,node = q.popleft()
            print(cur,node)
            if node ==endWord:
                return cur+1
            for nex in  data[node]:
                if nex not in seen:
                    q.append((cur+1,nex))
                    seen.add(nex)
        return 0
