class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # 初期コストを無限大に設定
        costs = [float('inf')] * n
        costs[src] = 0
        
        # 経由数 k 回分、ループを回す (k + 1 回のステップ)
        for i in range(k + 1):
            temp_costs = costs[:] # 現在のステップの値を保存
            for u, v, price in flights:
                if costs[u] != float('inf'):
                    if temp_costs[v] > costs[u] + price:
                        temp_costs[v] = costs[u] + price
            costs = temp_costs
            
        return costs[dst] if costs[dst] != float('inf') else -1