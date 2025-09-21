from typing import List
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i >= len(nums):
                return 0
            
            ans = max(nums[i] + dp(i+2), dp(i+1))
            return ans

        return dp(0)
    
if __name__ == "__main__":
    runner = Solution()
    nums = [2,7,9,3,1]
    ans = runner.rob(nums)
    print(ans)
    print("exp ans:", 12)