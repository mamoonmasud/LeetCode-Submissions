class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestion = []
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        
        for product in products:
            self._insert(root, product)
            
        return self._search(root, searchWord)
    
    
    def _insert(self, root, product):
        cur  = root
        for ch in product:
            cur = cur.children.setdefault(ch, TrieNode())
            
            cur.suggestion.append(product)
            cur.suggestion.sort()
            if len(cur.suggestion)> 3:
                cur.suggestion.pop()
                
                
    def _search(self, root, searchW):
        
        cur = root
        res= []
        for ch in searchW:
            if cur:
                cur = cur.children.get(ch)
                
            if not cur:
                res.append([])
                
            else:
                res.append(cur.suggestion)
                
        return res