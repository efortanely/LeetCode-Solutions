class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def helper(first: int):
            if first == n:
                ans.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    helper(first + 1)
                    nums[i], nums[first] = nums[first], nums[i]
                    
        helper(0)
        return ans
