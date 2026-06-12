
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {c: set() for w in words for c in w}
        deg = {c: 0 for c in adj}
        for i in range(n-1):
            a,b  = words[i],words[i+1]
            minLen = min(len(a),len(b))
            # 辞書順に反している
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""
            for j in range(min(len(a),len(b))):
                if a[j]==b[j]:
                    continue
                if b[j] not in adj[a[j]]:
                    adj[a[j]].add(b[j])
                    deg[b[j]]+=1
                break
        
        q = deque([c for c in deg if deg[c] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nex in adj[node]:
                deg[nex]-=1
                if deg[nex]==0:
                    q.append(nex)
        if len(res) != len(deg):
            return ""

        return "".join(res)
