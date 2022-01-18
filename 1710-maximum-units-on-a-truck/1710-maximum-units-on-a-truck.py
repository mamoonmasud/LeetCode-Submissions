class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        
        boxTypes = [(-unit_num, box_num ) for box_num, unit_num in boxTypes]
        heapq.heapify(boxTypes)
        
        box_count = 0
        unit_cnt =0
        while(boxTypes):
            unit_n , box_n = heapq.heappop(boxTypes)
            
            if box_n + box_count<= truckSize:
                
                box_count += box_n
                unit_cnt += (-1*unit_n*box_n)
                
            else:
                unit_cnt += (-1*unit_n)*(truckSize-box_count)
                
                break
        return unit_cnt