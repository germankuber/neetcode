from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        left_moved = False
        while left < right:
            base = right - left
            max_high = 0
            if heights[left] < heights[right]:
                max_high = heights[left]
                left += 1
            else:
                max_high = heights[right]
                right -= 1
                
            area = base * max_high
            
            if area > max_area:
                    max_area = area
        
        return max_area
            
            