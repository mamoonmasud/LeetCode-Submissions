# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         @lru_cache(maxsize = None)
        
#         def rec(s, i):
#             for j in range(i+1, len(s)):
#                 if s[i:j] in wordSet and rec(s, j):
#                     return 2
#             if s[i:] in wordSet:
#                 return 1
#             return 0
        
#         wordSet = set(words)
#         ret = []
        
#         for word in words:
#             if rec(word, 0)==2:
#                 ret.append(word)
#         return ret


## Trie Solution

class Trie:
    def __init__(self):
        self.root = dict()
        
    def insert(self, words):
        for word in words:
            current = self.root
            for char in word:
                if char not in current:
                    current[char] = dict()
                    
                current = current[char]
            current["*"] = "*"
            
            
    @lru_cache()
    
    def search(self, target):
        if target == "":
            return True
        
        result = False
        node = self.root
        
        for idx, char in enumerate(target):
            if char not in node:
                break
            node= node[char]
            
            if "*" in node:
                result = result or self.search(target[idx+1:])
                if result:
                    break
                    
        return result
    
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        obj = Trie()
        obj.insert(words)
        final = []
        
        final =[]
        
        for word in words:
            node = obj.root
            for idx, char in enumerate(word):
                node = node[char]
                
                if "*" in node:
                    if idx != len(word)-1 and obj.search(word[idx+1:]):
                        final.append(word)
                        break
                        
        return final
                    
                    