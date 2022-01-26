class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        @lru_cache(maxsize = None)
        
        def rec(s, i):
            for j in range(i+1, len(s)):
                if s[i:j] in wordSet and rec(s, j):
                    return 2
            if s[i:] in wordSet:
                return 1
            return 0
        
        wordSet = set(words)
        ret = []
        
        for word in words:
            if rec(word, 0)==2:
                ret.append(word)
        return ret