class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) < 2:
            return 0
        
        heapq.heapify(sticks)
        total_c = 0
        cost_x = 0
        while(len(sticks)>1):
            stick_1 = heapq.heappop(sticks)
            stick_2 = heapq.heappop(sticks)
            cost_x= stick_1 + stick_2
            total_c += cost_x
            
            heapq.heappush(sticks, cost_x)
            
        return total_c