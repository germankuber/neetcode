class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        
        
        while right + 1 - left > k:
            
            left_distance = abs(arr[left] - x)
            right_distance = abs(arr[right] - x)
            
            if left_distance > right_distance:
                left += 1
            else:
                right -= 1
                
        return arr[left: right + 1]