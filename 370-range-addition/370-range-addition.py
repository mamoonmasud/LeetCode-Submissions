class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length
        
        
        for update in updates:
            
            start, end , val = update
            res[start] += val
            if end +1 <len(res):
                res[end+1] -= val
                
                
                
                
        for i in range(1, length):
            res[i] += res[i-1]
            
        return res
        