from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0

        for num in nums:
            x ^= num

        return x

if __name__ == "__main__":
    runner = Solution()
    nums = [4,1,2,1,2]
    ans = runner.singleNumber(nums)
    print(ans)