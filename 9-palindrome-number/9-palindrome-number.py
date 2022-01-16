class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        list_x = []
        div , remainder = 0, 0
        
        if x<0:
            return 0
        
        while (x!=0):
            remainder = x%10
            list_x.append(remainder)
            div = x//10
            x = div
            
        return (1 if list_x == list_x[::-1] else 0)
            
            