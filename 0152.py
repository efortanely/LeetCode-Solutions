class Solution:
    '''
    def maxProduct(self, nums: List[int]) -> int:
        M_max = [nums[0] for n in range(len(nums))]
        M_min = [nums[0] for n in range(len(nums))]
        for i in range(1, len(nums)):
            M_max[i] = max(max(M_max[i-1] * nums[i], M_min[i-1] * nums[i]), nums[i])
            M_min[i] = min(min(M_max[i-1] * nums[i], M_min[i-1] * nums[i]), nums[i])

        return max(max(M_max), max(M_min))
    '''
    def maxProduct(self, nums: List[int]) -> int:
        M_max = nums[0]
        M_min = nums[0]
        max_val = nums[0]
        for i in range(1, len(nums)):
            temp = M_max
            M_max = max(max(M_max * nums[i], M_min * nums[i]), nums[i])
            M_min = min(min(temp * nums[i], M_min * nums[i]), nums[i])
            max_val = max(max(max_val, M_max), M_min)
        return max_val
