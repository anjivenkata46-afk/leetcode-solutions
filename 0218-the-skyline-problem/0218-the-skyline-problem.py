import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for left, right, height in buildings:
            # Start event: negative height so max-heap acts like max-heap, 
            # and start events come before end events at the same x-coordinate
            events.append((left, -height, right))
            # End event: positive height
            events.append((right, 0, 0))
            
        # Sort events by x-coordinate. If x matches, sort by height accordingly.
        events.sort()
        
        # Result list for key points, and heap to track active building heights
        result = [[0, 0]]
        # Store active heights: store (-height, right_coordinate)
        max_heap = [(0, float('inf'))]
        
        for x, neg_height, right in events:
            # 1. Remove buildings that have already ended (their right edge <= current x)
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
                
            # 2. If it's a building start event, add it to the active heap
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, right))
                
            # 3. If the current max height has changed, record a key point
            current_max_height = -max_heap[0][0]
            if result[-1][1] != current_max_height:
                result.append([x, current_max_height])
                
        return result[1:]