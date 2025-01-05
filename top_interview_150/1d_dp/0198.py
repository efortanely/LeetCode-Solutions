from typing import List
from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i, money):
            if i < 0:
                return money

            return max(dp(i-2, money + nums[i]), dp(i-1, money))

        ans = dp(len(nums)-1, 0)
        return ans
    
if __name__ == "__main__":
    runner = Solution()
    nums = [2,7,9,3,1]
    ans = runner.rob(nums)
    print(ans)