class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        nodes = defaultdict(list)
        for a, b in tickets:
            nodes[a].append(b)
        for i,v in nodes.items():
            nodes[i].sort(reverse=True)
        print(nodes)
 
        res = []
        def dfs(src):
            print(src,res)
            while nodes[src]:
                dst = nodes[src].pop()
                dfs(dst)
            res.append(src)
        dfs('JFK')
        return res[::-1]