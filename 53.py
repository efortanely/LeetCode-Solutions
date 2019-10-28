class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M = [(-sys.maxsize - 1) for n in range(len(nums) + 1)]
        #Case 1: Insert the value in the subarray
        #Case 2: Start a new subarray at the value
        for i in range(len(nums)):
            M[i] = max(M[i-1] + nums[i], nums[i])
        return max(M)
