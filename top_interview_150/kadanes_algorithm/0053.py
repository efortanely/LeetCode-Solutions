from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_subarray_sum = float("-inf")
        ans = float("-inf")

        for i in range(len(nums)):
            cur_subarray_sum = max(cur_subarray_sum + nums[i], nums[i])
            ans = max(ans, cur_subarray_sum)
        
        return ans

if __name__ == "__main__":
    runner = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = runner.maxSubArray(nums)
    print(ans)