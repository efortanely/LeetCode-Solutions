class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i+1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum is 0:
                    triplet = (nums[i], nums[l], nums[r])
                    ans.add(triplet)
                    l += 1
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
        
        return list(ans)
