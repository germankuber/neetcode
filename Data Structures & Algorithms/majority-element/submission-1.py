class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_size = len(nums) // 2
        elements = {}
        for num in nums:
            if num not in elements:
                elements[num] = 0
            elements[num] += 1

        for key in elements.keys():
            if elements[key] > majority_size:
                return key
            
        