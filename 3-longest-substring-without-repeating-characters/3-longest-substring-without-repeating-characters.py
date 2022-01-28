class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        l = 0
        r = 1
        x = len(s)
        if x<2:
            return x
        max_len = 0
        substring.add(s[0])
        while(r<x):
            if s[r] not in substring:
                substring.add(s[r])
                max_len = max(max_len, r-l+1 )
                r+=1
            else:
                substring.remove(s[l])
                l+=1
        return (max_len)    
        