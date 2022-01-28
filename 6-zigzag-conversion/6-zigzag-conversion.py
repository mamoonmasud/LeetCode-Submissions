class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
#         if numRows ==1:
#             return s
#         res = ['']*numRows
        
#         i, dif = 0 , True
#         for c in s:
#             res[i]+=c
#             if i ==0:
#                 dif = 1
#             elif i == numRows-1:
#                 dif = -1
#             i+= dif
#         print(res)
#         return ''.join(res)

        rows, direction, i = [[] for x in range(numRows)], 1, 0
        
        for char in s:
            rows[i].append(char)
            i = min(numRows-1, max(0, i + direction))
            if i ==0 or i == numRows - 1:
                direction *= -1
        
        return ''.join(''.join(row) for row in rows)