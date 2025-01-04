class Solution:
    def rob(self, nums: List[int]) -> int:
        #Case 1: Don't steal from the house you are at
        #Case 2: Steal from the house 2 positions behind you and the house you're currently at
        if len(nums) is 0:
            return 0
        
        M = [0 for n in range(len(nums))]
        for i in range(len(nums)):
            val = M[i-2] if i-2 >= 0 else 0
            M[i] = max(M[i-1], val + nums[i])
        return M[-1]
