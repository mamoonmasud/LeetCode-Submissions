class MaxHeap:
    def __init__(self):
        self.queue = []
        
    def __len__(self):
        return len(self.queue)
    
    def top(self):
        if len(self.queue)==0:
            return 0
        return self.queue[0]* -1
    
    def push(self, val):
        heapq.heappush(self.queue, -val)
        
    def pop(self):
        return heapq.heappop(self.queue)*-1

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        ballC = 1
        maxHeap = MaxHeap()
        
        for ball in inventory:
            maxHeap.push(ball)
            
        maxBallV = maxHeap.pop()
        
        while len(maxHeap) and maxHeap.top() == maxBallV:
            ballC +=1 
            maxHeap.pop()
            
        totalCost = 0
        
        while orders:
            difference = ballC *(maxBallV  - maxHeap.top())
            
            if difference >= orders:
                rounds = orders //ballC
                totalCost += ballC *rounds*(2*maxBallV - rounds +1)//2
                orders -= rounds * ballC
                
                if orders >0:
                    totalCost += orders* (maxBallV - rounds)
                    
                return totalCost%(10**9 + 7)
            
            else:
                rounds = difference // ballC
                totalCost += ballC *rounds * (2*maxBallV -rounds +1)//2
                maxBallV = maxBallV - rounds
                orders -=difference
                
                
            while len(maxHeap) and maxHeap.top() == maxBallV:
                ballC +=1
                maxHeap.pop()
                
        return totalCost %(10**9 +7)
                