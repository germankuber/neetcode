class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product_left = [1] * length
        product_right = [1] * length
        result = [1] * length
        
        for index in range(1, length):
            num =  nums[index - 1]
            num_left = product_left[index - 1] 
            product_left[index] = num_left * num
        
        for index in range(length - 2, -1, -1):
            num =  nums[index + 1]
            num_left = product_right[index + 1] 
            product_right[index] = num_left * num 
        
        
        for index, value in enumerate(product_left):
            result[index] =  value * product_right[index]
        return result