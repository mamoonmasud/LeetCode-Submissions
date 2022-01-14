class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        now  =0
        flag = s[0]
        
        prev = 0
        
        total_com =0 
        
        for x in s:
            if x == flag:
                now += 1
            else:
                total_com += min(now, prev)
                
                prev = now
                now, flag = 1, x
                
        total_com += min(now, prev)
        
        return total_com