from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = set(range(len(nums) + 1))
        return all_nums.difference(set(nums)).pop()

if __name__ == "__main__":
    nums = [3,0,1]
    ans = Solution().missingNumber(nums)
    print(ans)