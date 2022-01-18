class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        webinfo = []
        
        for i in range(len(username)):
            webinfo.append([username[i], timestamp[i], website[i]])
    
        #Sorting the list by Time Stamp!
        webinfo.sort(key = lambda x: x[1])
        
        h = defaultdict(list)
        
        for i in range(len(webinfo)):
            h[webinfo[i][0]].append(webinfo[i][2])
            
            
        counts = defaultdict(int)
        maxcount = 0
        for user in h:
            v = h[user]
            n = len(v)
            
            visited = set()
            
            for i in range(n-2):
                for j in range(i+1, n-1):
                    for k in range(j+1, n):
                        tup = (v[i], v[j], v[k])
                        
                        if tup not in visited:
                            visited.add(tup)
                            counts[tup] +=1
                            maxcount = max(maxcount, counts[tup])
                            
        res = []
        
        for tup in counts:
            if counts[tup] == maxcount:
                res.append(tup)
                
                
        return(sorted(res)[0])

                