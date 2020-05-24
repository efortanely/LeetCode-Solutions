class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero = []
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero.append(nums[i])
        
        for i in range(len(nums)):
            if i < len(non_zero):
                nums[i] = non_zero[i]
            else:
                nums[i] = 0
        
