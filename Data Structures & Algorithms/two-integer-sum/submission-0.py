class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_check = {}
        
        for index,num in enumerate(nums):
            value_to_check = target - num
            if value_to_check in nums_to_check:
                return [nums_to_check[value_to_check], index]
            else:
                nums_to_check[num] = index

        return False