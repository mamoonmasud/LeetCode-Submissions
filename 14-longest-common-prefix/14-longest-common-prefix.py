class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sub = []
        
        i = 0
        x = [len(i) for i in strs]
        y = min(x)
        for i in range(y):
            prev = strs[0][i]
            for word in strs:
                if word[i] != prev:
                    return ''.join(sub)
            sub.append(prev)
            
        return ''.join(sub)
                
            