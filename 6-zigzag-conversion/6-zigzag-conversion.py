class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        res = ['']*numRows
        
        i, dif = 0 , True
        for c in s:
            res[i]+=c
            if i ==0:
                dif = 1
            elif i == numRows-1:
                dif = -1
            i+= dif
        print(res)
        return ''.join(res)