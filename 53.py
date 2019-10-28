class Solution:
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        M = [(-sys.maxsize - 1) for n in range(len(nums) + 1)]
        #Case 1: Insert the value in the subarray
        #Case 2: Start a new subarray at the value
        for i in range(len(nums)):
            M[i] = max(M[i-1] + nums[i], nums[i])
        return max(M)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -sys.maxsize - 1
        prev_val = max_val
        #Case 1: Insert the value in the subarray
        #Case 2: Start a new subarray at the value
        for i in range(len(nums)):
            prev_val = max(prev_val + nums[i], nums[i])
            max_val = max(max_val, prev_val)
        return max_val
