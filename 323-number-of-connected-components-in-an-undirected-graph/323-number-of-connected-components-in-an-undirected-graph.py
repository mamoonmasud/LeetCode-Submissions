class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         visit = set()
        
#         adj = {i: [] for i in range(n)}
#         for n1, n2 in edges:
#             adj[n1].append(n2)
#             adj[n2].append(n1)
            
#         def dfs(node, prev):
#             if node in visit:
#                 return 
#             visit.add(node)
#             for neigh in adj[node]:
#                 if neigh == prev:
#                     continue
#                 else:
#                     dfs(neigh, node)
                    
#             return
#         connected_comp = 0
#         for i in range(n):
#             if i not in visit:
#                 dfs(i, -1)
#                 connected_comp+=1 
                
#         return connected_comp
            
                
        parent = [i for i in range(n)]
        rank = [1]*n
        
        def find(n1):
            res = n1
            while (res != parent[res]):
                parent[res] = parent[parent[res]] 
                res = parent[res]
                
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        
        for n1, n2 in edges:
            res -= union(n1, n2)
            
        return res