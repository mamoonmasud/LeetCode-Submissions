class Trie:
    def __init__(self):
        self.children= {}
        self.word = False
        
        
class WordDictionary:
    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word):
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
                
            curr= curr.children[c]
            
        curr.word = True
        
        
    def search(self, word: str) ->bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                        
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                    
            return curr.word
        return dfs(0, self.root)
    
        
        
            