class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit = []
        
        for log in logs:
            if not log[-1].isalpha():
                digit.append(log)
            else:
                letter.append(log)
        def sorting_algo(log):
            left_side, right_side = log.split(" ", 1)
            return (0, right_side , left_side)
        
        letter.sort(key = sorting_algo)        
        
        
        return letter + digit
        