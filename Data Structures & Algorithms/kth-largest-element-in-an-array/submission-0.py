import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # nuestra "cajita"
        
        for num in nums:
            if len(heap) < k:
                # todavía hay lugar → entra sin preguntar
                heapq.heappush(heap, num)
            elif num > heap[0]:
                # cajita llena y el nuevo es mejor que el peor → cambio
                heapq.heappushpop(heap, num)
            # si no, descarto (no hago nada)
        
        return heap[0]  # el peor de los k mejores = k-ésimo más grande
                
            