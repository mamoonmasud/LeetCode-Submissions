class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        memo = defaultdict(list)
        for idx, char in enumerate(s):
            memo[char].append(idx)
            
        result = 0
        
        for key, val in memo.items():
            for i, idx in enumerate(val):
                if i-1 >=0:
                    left = idx - val[i-1]
                else:
                    left = idx - (-1)
                    
                if i+1 < len(val):
                    right = val[i+1] - idx
                else:
                    right = len(s) - idx
                
                result += left*right
        return result
#         if s is None:
#             return 
        
#         lastSeen = {}
#         count_sub = 0
        
#         last_s_cnt = 0
        
#         for i in range(len(s)):
#             last_two_idx = lastSeen.get(s[i], None)
            
#             if not last_two_idx:
#                 crnt_s_cnt = last_s_cnt + i + 1
                
#                 lastSeen[s[i]] = (-1, i)
                
#             else:
#                 snd_lst_s_idx , last_s_idx = last_two_idx
                
#                 num_of_suffix_without = i - 1 - last_s_idx
#                 num_of_suffix_with_one = last_s_idx -  snd_lst_s_idx
                
#                 crnt_s_cnt = last_s_cnt +  1 + num_of_suffix_without - num_of_suffix_with_one
                
#                 lastSeen[s[i]] = (last_s_idx, i)
            
            
            
#             count_sub += crnt_s_cnt
#             last_s_cnt = crnt_s_cnt
            
#         return count_sub