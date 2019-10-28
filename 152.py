class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        M_max = [nums[0] for n in range(len(nums))]
        M_min = [nums[0] for n in range(len(nums))]
                                        
        #Case 1: Insert the value in the subarray
        #Case 2: Start a new subarray at the value
        for i in range(1, len(nums)):
            M_max[i] = max(max(M_max[i-1] * nums[i], M_min[i-1] * nums[i]), nums[i])
            M_min[i] = min(min(M_max[i-1] * nums[i], M_min[i-1] * nums[i]), nums[i])

        return max(max(M_max), max(M_min))
