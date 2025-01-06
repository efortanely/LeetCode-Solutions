from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = float("-inf")
        ans = float("-inf")

        for num in nums:
            curr_sum = max(curr_sum + num, num)
            ans = max(ans, curr_sum)
        
        return ans

if __name__ == "__main__":
    runner = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = runner.maxSubArray(nums)
    print(ans)