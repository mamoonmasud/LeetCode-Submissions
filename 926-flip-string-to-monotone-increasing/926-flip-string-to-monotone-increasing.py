class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones= 0
        flips = 0
        
        for c in s:
            if c =="0" and ones >0:
                flips +=1
                ones -=1
                
            elif c=="1":
                ones+=1 
                
        return flips