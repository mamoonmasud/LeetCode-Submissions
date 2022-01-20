class Solution:

    def minSwaps(self, data: List[int]) -> int:

#         ones = sum(data)
#         if ones <= 1:
#             return 0
#         minswaps = ones
#         w = deque(maxlen = ones)
        
#         curr = 0
        
#         for b in data:
#             if len(w) == ones:
#                 curr -= w[0]
                
#             w.append(b)
#             curr += b
#             if len(w) == ones:
#                 minswaps = min(minswaps, ones - curr)
                
#         return min(minswaps, ones - curr)
    
        ones = sum(data)
        if ones <2:
            return 0
        start = 0
        end = ones-1
        
        zeros = data[start:ones].count(0)
        
        minswap = zeros
        while end < len(data) -1:
            prev = data[start]
            start +=1
            end +=1
            
            cur = data[end]
            if cur ==1 and prev == 0:
                zeros -=1
                
            elif cur ==0 and prev ==1:
                zeros+=1
            minswap = min(minswap, zeros)
            
        return minswap