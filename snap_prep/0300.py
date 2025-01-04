class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        M = [0 for n in range(len(nums))]
        M[0] = 1
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    M[i] = max(M[i], M[j])
            M[i] += 1
        
        return max(M)
