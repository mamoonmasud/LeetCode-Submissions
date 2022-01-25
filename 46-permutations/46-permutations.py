class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= [] #Result Array
        
        def dfs(curr, i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    dfs(curr, i+1)
                    curr.pop()
                    
                    
        dfs([], 0)
        
        return res
        
        