class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        
        for index in range(len(nums)):
            if nums[index] != val:
                nums[k] = nums[index]
                k += 1
        return k
                