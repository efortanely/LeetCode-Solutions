from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor) -> bool:
            return sum([ceil(num/divisor) for num in nums]) <= threshold
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

def main():
    runner = Solution()

    nums = [1,2,5,9]
    threshold = 6
    ans = runner.smallestDivisor(nums, threshold)
    print(ans)

if __name__ == "__main__":
    main()