from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        
        for num in nums:
            if num not in numbers:
                numbers[num] = 0
            numbers[num] += 1

        heap = []    

        for values in  numbers.items():
            number_to_evaluate = values[0]
            number_count = values[1]
            if len(heap) >= k:
                first = heapq.heappop(heap)    
                if first[0] > number_count:
                    heapq.heappush(heap,first)
                else:
                    
                    heapq.heappush(heap, (number_count, number_to_evaluate))
            else: 
                heapq.heappush(heap, (number_count, number_to_evaluate))
        
        return [value[1] for value in heap]