class Solution:

    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        if ones <= 1:
            return 0
        minswaps = ones
        w = deque(maxlen = ones)
        
        curr = 0
        
        for b in data:
            if len(w) == ones:
                curr -= w[0]
                
            w.append(b)
            curr += b
            if len(w) == ones:
                minswaps = min(minswaps, ones - curr)
                
        return min(minswaps, ones - curr)