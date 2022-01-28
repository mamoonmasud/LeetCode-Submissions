class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        
        l = 0
       
        max_f = 0
        count =0
        for i in range(len(s)):
            freq[s[i]] = 1 + freq.get(s[i], 0)
            max_f = max(max_f, freq[s[i]])
            
            while (i-l+1) - max_f > k:
                freq[s[l]] -= 1
                l+=1
                
            count = max(i-l+1, count)

        return count