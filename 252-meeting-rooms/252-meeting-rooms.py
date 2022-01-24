class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        if len(intervals)<2:
            return True
        prev_end = intervals[0][1]
        cur_start = 0
        cur_end = 0
        for i in range(1, len(intervals)):
            cur_start , cur_end =  intervals[i][0], intervals[i][1]
            
            if cur_start<prev_end:
                return False
            prev_end = cur_end
        return True