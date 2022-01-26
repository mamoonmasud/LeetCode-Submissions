class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        
        prev_end = None
        
        intervals = sorted(intervals, key = lambda i: i[0])
        
        out = []
        s_start, s_end = 0, 0
        
        for c_start, c_end in intervals:
            
            #Initial Condition
            if prev_end == None:
                s_start = c_start

                prev_end = c_end
                
            #Overlapping condition
            
            if c_start <= prev_end:
                s_end = max(s_end, c_end)
                s_start= min(s_start, c_start)
                prev_end = s_end
                #print(s_start, s_end)
            
            # Non-overlap condition
            elif c_start >  prev_end:
                out.append([s_start, s_end])
                prev_end = c_end
                s_start = c_start
                s_end = c_end
                
        out.append([s_start, s_end])
        return out
                
                