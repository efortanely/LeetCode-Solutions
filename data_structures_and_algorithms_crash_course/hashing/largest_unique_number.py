from typing import List
from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        largest_num = max([key for key, val in counts.items() if val == 1] + [-1])
        return largest_num
    
def main():
    runner = Solution()

    nums = [9,9,8,8]
    ans = runner.largestUniqueNumber(nums)
    print(ans)

if __name__ == "__main__":
    main()