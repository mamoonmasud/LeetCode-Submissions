class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        
#         now  =0
#         flag = s[0]
        
#         prev = 0
        
#         total_com =0 
        
#         for x in s:
#             if x == flag:
#                 now += 1
#             else:
#                 total_com += min(now, prev)
                
#                 prev = now
#                 now, flag = 1, x
                
#         total_com += min(now, prev)
        
#         return total_com

        ones, zeros, count = 0, 0, 0
    
        for i in range(len(s)):
            if s[i] == '0':
                zeros = 1 if i>0 and s[i-1]!="0" else zeros+1
                
                if zeros <=ones:
                    count+=1
            else:
                ones = 1 if i >0 and s[i-1] != '1' else ones + 1
                if ones <= zeros:
                    count+=1
                    
        return count