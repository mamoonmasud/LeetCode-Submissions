class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        def dfs(node, prev):
            if node in visit:
                return 
            visit.add(node)
            for neigh in adj[node]:
                if neigh == prev:
                    continue
                else:
                    dfs(neigh, node)
                    
            return
        connected_comp = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                connected_comp+=1 
                
        return connected_comp
            
                
        