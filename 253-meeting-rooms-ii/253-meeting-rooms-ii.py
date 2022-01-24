class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        
        h = []
        maxRooms = 0
        for i in range(len(intervals)):
            if not h:
                heapq.heappush(h, intervals[i][1])
                
            else:
                while h and intervals[i][0] >= h[0]:
                    heapq.heappop(h)
                    
                heapq.heappush(h, intervals[i][1])
                
            maxRooms = max(maxRooms, len(h))
            
        return maxRooms