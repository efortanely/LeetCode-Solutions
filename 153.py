class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) is 1:
            return nums[0]
        
        k = len(nums)//2
        left = nums[0:k]
        right = nums[k:]
        
        return self.findMin(right) if not left or left[-1] > right[-1] else self.findMin(left)
