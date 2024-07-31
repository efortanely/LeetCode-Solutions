from typing import List
from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i >= len(nums) - 1:
                return True
            
            for j in range(1, nums[i] + 1):
                if dp(i+j):
                    return True
            return False

        return dp(0)

def main():
    runner = Solution()
    nums = [1,2,3]
    ans = runner.canJump(nums)
    print(ans)

if __name__ == "__main__":
    main()