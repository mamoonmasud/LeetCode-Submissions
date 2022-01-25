class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score= 0
        tokens.sort()
        
        a = deque(tokens)
        res =0
        
        while a and (power or score):
            if power < a[0]:
                if not score:
                    return res
                score -=1
                power+= a.pop()
                
                
            else:
                power -= a.popleft()
                score += 1
                
            res = max(res, score)
            
        return res
         