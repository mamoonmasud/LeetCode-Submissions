class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cur_i = 0
        for i in range(1, n+1):
            if n%i==0:
                cur_i +=1
                if cur_i == k:
                    return i
        return -1