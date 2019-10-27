class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        M1 = [1 for x in range(len(nums) + 1)]
        M2 = [1 for x in range(len(nums) + 1)]
        nums2 = []
        
        for i in range(len(nums)):
            M1[i] = M1[i-1] * nums[i]
            
        for i in range(len(nums) - 1, -1, -1):
            M2[i] = M2[i+1] * nums[i]
                        
        for i in range(len(nums)):
            nums2.append(M1[i-1] * M2[i+1])
        
        return nums2
