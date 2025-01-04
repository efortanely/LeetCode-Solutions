class Solution:
    def rob(self, nums: List[int]) -> int:    
        if len(nums) is 0:
            return 0
        elif len(nums) is 1:
            return nums[0]
        elif len(nums) is 2:
            return max(nums)
        
        return max([self.rob_helper(nums[:-1]), self.rob_helper(nums[1:])])
    
    def rob_helper(self, nums: List[int]) -> int:    
        if len(nums) is 0:
            return 0
        
        M = [0 for n in range(len(nums))]
        for i in range(len(nums)):
            val = M[i-2] if i-2 >= 0 else 0
            M[i] = max(M[i-1], val + nums[i])
        return M[-1]
