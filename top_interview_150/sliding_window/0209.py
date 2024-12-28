from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_size = float("inf")
        sum = 0

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                min_size = min(min_size, right - left + 1)
                sum -= nums[left]
                left += 1

        return min_size if min_size != float("inf") else 0

if __name__ == "__main__":
    runner = Solution()
    target = 7
    nums = [1,1,1,1,1,1,1,1]
    ans = runner.minSubArrayLen(target, nums)
    print(ans)
