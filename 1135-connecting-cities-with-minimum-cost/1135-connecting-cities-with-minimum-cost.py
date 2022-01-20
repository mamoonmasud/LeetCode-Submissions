class Solution:
    def find (self, node, par):
        while node != par[node]:
            par[node] = par[par[node]]
            node = par[node]
        return node
    
    def union(self, par, left, right ):
        if par[left] < par[right]:
            par[right] = par[left]
        else:
            par[left] = par[right]
        return par
      
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        cost_first = [(cost, left, right) for left, right, cost in connections]
        heapq.heapify(cost_first)
        par = [i for i in range(n+1)]
        
        totalcost = 0
        connections = 0
        
        while cost_first:
            cost, left, right = heapq.heappop(cost_first)
            
            r_left = self.find(left, par)
            r_right = self.find(right, par)
            
            if r_right != r_left:
                par = self.union(par, r_left, r_right)
                totalcost += cost
                connections += 1
                
            if connections == n-1:
                return totalcost
            
        if len(set(par[1:])) != 1:
            return -1