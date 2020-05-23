class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, target, 0)
    
    def search_helper(self, nums: List[int], target: int, idx: int) -> int:
        if len(nums) is 0:
            return -1
        elif nums[0] == target:
            return idx
        
        k = len(nums)//2
        left = nums[0:k]
        right = nums[k:]
        
        if left and left[0] <= target <= left[-1]:
            return self.search_helper(left, target, idx)
        elif right and right[0] <= target <= right[-1]:
            return self.search_helper(right, target, idx+k)
        elif right[0] > right[-1]:
            return self.search_helper(right, target, idx+k)
        else:
            return self.search_helper(left, target, idx)
